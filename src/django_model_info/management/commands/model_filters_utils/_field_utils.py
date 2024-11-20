"""Utilities for working with fields in Django models.

Modified from utils.py in django-drip-campaigns.
"""
import re
from dataclasses import dataclass
from datetime import timedelta
from typing import NamedTuple, Optional, TypeVar

from django.apps import apps
from django.db import models
from django.db.models import F, Field, ForeignKey, ManyToManyField, OneToOneField
from django.db.models.fields.related import ForeignObjectRel as RelatedObject

AbstractQuerySetRule = TypeVar("AbstractQuerySetRule")
TimeDeltaOrStr = timedelta | str
BoolOrStr = bool | str
FExpressionOrStr = F | str
FieldValue = TimeDeltaOrStr | BoolOrStr | FExpressionOrStr
FieldType = Field | ForeignKey | OneToOneField | RelatedObject | ManyToManyField
ModelInput = type[models.Model]|str
basestring = (str, bytes)


class FieldNotFoundError(Exception):
    """Custom exception for when a field is not found."""


class FieldInfo(NamedTuple):
    """Represents field information in a structured way."""

    full_field: str
    model_name: str
    field_name: str
    field_type: str
    model_path: str


@dataclass
class FilterConfig:
    """Configuration for field filtering."""

    excludes: list[str]
    max_depth: Optional[int]
    max_paths: Optional[int]
    field_type: Optional[str]
    target_model: Optional[type[models.Model]]
    target_field: Optional[str]


@dataclass
class PathTracker:
    """Tracks path-related data during field traversal."""

    seen: set[tuple[str, str, str, str]]
    result_count: list[int]
    model_stack: list[type[models.Model]]
    stack_limit: int

    @classmethod
    def create(cls, stack_limit: int = 2) -> "PathTracker":
        """Create a new PathTracker instance with default values."""
        return cls(seen=set(), result_count=[0], model_stack=[], stack_limit=stack_limit)


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub("([A-Z])([A-Z][a-z])", r"\1_\2", name).lower()


def normalize_exclude_pattern(pattern: str) -> str:
    """Normalize exclusion pattern to handle various input formats.

    Examples:
    - model_name -> model_name
    - ModelName -> model_name
    - app_name.ModelName -> model_name
    - field_name -> field_name
    """
    if "." in pattern:
        _, model_name = pattern.split(".")
        return camel_to_snake(model_name)
    return camel_to_snake(pattern)


def normalize_field_path(field_path: str) -> str:
    """Normalize field path for comparison with exclude patterns.

    Handles paths like: model_name__related_name__field_name
    """
    return "__".join(camel_to_snake(part) for part in field_path.split("__"))


def normalize_model_name(name: str) -> str:
    """Normalize a model name to a consistent format.

    Examples:
        - UserProfile -> user_profile
        - user_profile -> user_profile
        - User -> user
    """
    return camel_to_snake(name)


def normalize_app_model(pattern: str) -> tuple[Optional[str], Optional[str]]:
    """Split and normalize an app.Model pattern.

    Examples:
        - auth.Permission -> (auth, permission)
        - Permission -> (None, permission)
        - auth -> (auth, None)
    """
    if "." in pattern:
        app, model = pattern.split(".")
        return app.lower(), normalize_model_name(model) if model else None
    return None, normalize_model_name(pattern)


def get_model_from_input(model_input: ModelInput) -> type[models.Model]:
    """Convert model input to a Django model class."""
    if isinstance(model_input, basestring):
        if "." in model_input:
            app_label, model_name = model_input.split(".")
            return apps.get_model(app_label, model_name)
        return next(
            (model for model in apps.get_models() if model.__name__ == model_input),
            None,
        )
    return model_input


def check_redundant(model_stack: list[type[models.Model]], stack_limit: int, max_depth: int = None) -> bool:
    """Checks to ensure recursion isn't being redundant."""
    if max_depth is not None and len(model_stack) > max_depth:
        return True

    stop_recursion = False
    if len(model_stack) > stack_limit:
        if (
            (model_stack[-3] == model_stack[-1])
            or (len(model_stack) > 7)
            or (len(set(model_stack)) != len(model_stack))
        ):
            stop_recursion = True
    return stop_recursion


def get_field_name(field: FieldType) -> str:
    """Get the field name from a field object."""
    field_name = field.name
    if isinstance(field, RelatedObject):
        field_name = field.field.related_query_name()
    return field_name


def get_full_field(parent_field: str, field_name: str) -> str:
    """Get the full field name from a parent field and a field name."""
    if parent_field:
        full_field = "__".join([parent_field, field_name])
    else:
        full_field = field_name
    return full_field


def get_rel_model(field: FieldType) -> type[models.Model]:
    """Get the related model from a field object."""
    if not is_valid_instance(field):
        RelModel = field.model
    else:
        RelModel = field.related_model
    return RelModel


def is_valid_instance(field: FieldType) -> bool:
    """Check if the field is a valid instance."""
    return isinstance(field, (ForeignKey, OneToOneField, RelatedObject, ManyToManyField))


def should_skip_field(full_field: str, model_name: str, model_path: str, excludes: list[str]) -> bool:
    """Check if field should be skipped based on exclusion rules.

    Args:
        full_field: The field path (e.g. 'customer__user__logentry__content_type')
        model_name: The name of the current model
        model_path: Comma-separated string of app.Model labels in the path
        excludes: List of patterns to exclude

    Examples:
        - Exclude by model name: 'Permission'
        - Exclude by app.model: 'auth.Permission'
        - Exclude by field path: 'user__profile'
    """
    if not excludes:
        return False

    # Normalize the current field information
    normalized_field_path = normalize_model_name(full_field)
    normalized_current_model = normalize_model_name(model_name)

    # Get list of all models in the path with their apps
    model_paths = model_path.split(",")

    for exclude_pattern in excludes:
        # Case 1: Exclude by field path (e.g., user__profile)
        if "__" in exclude_pattern:
            if exclude_pattern.lower() in normalized_field_path:
                return True

        # Case 2: Exclude by app.Model (e.g., auth.Permission)
        elif "." in exclude_pattern:
            exclude_app, exclude_model = exclude_pattern.split(".")
            exclude_app = exclude_app.lower()
            normalized_exclude_model = normalize_model_name(exclude_model)

            # Check if any model in the path matches this app.Model combination
            for path in model_paths:
                if "." in path:
                    path_app, path_model = path.split(".")
                    if path_app.lower() == exclude_app and normalize_model_name(path_model) == normalized_exclude_model:
                        return True

        # Case 3: Exclude by model name only (e.g., Permission)
        else:
            normalized_exclude = normalize_model_name(exclude_pattern)
            # Check both the current model and models in the path
            for path in model_paths:
                if "." in path:
                    _, path_model = path.split(".")
                    if normalize_model_name(path_model) == normalized_exclude:
                        return True

            # Also check the current model
            if normalized_exclude == normalized_current_model:
                return True

    return False


def matches_field_type(field: FieldType, field_type: Optional[str]) -> bool:
    """Check if field matches the specified field type."""
    return field_type is None or field.__class__.__name__ == field_type


def matches_target_filters(
    model: type[models.Model],
    field_name: str,
    target_model: Optional[type[models.Model]],
    target_field: Optional[str | list[str]],
) -> bool:
    """Check if field matches target model and field filters."""
    if target_model and model.__name__ != target_model.__name__:
        return False
    if target_field:
        if isinstance(target_field, list):
            return field_name in target_field
        return field_name == target_field
    return True


def create_field_info(
    field: FieldType, parent_field: str, model: type[models.Model], model_path: list[str]
) -> FieldInfo:
    """Create a FieldInfo instance from field data."""
    field_name = get_field_name(field)
    full_field = get_full_field(parent_field, field_name)
    # Join model path with commas
    model_path_str = ",".join(model_path + [model._meta.label])

    return FieldInfo(
        full_field=full_field,
        model_name=model.__name__,
        field_name=field_name,
        field_type=field.__class__.__name__,
        model_path=model_path_str,
    )


def process_field(
    field: FieldType,
    parent_field: str,
    model: type[models.Model],
    path_tracker: PathTracker,
    filter_config: FilterConfig,
    model_path: list[str],
) -> list[list[str]]:
    """Process a single field and return its field information if it matches filters."""
    field_info = create_field_info(field, parent_field, model, model_path)

    # Skip if we've seen this field
    if tuple(field_info[:-1]) in path_tracker.seen:  # Exclude model_path from uniqueness check
        return []

    # Check if field should be excluded
    if should_skip_field(field_info.full_field, field_info.model_name, field_info.model_path, filter_config.excludes):
        return []

    # Check if field matches all filters
    if not (
        matches_field_type(field, filter_config.field_type)
        and matches_target_filters(model, field_info.field_name, filter_config.target_model, filter_config.target_field)
    ):
        return []

    # Add field to results if we haven't exceeded max_paths
    if not filter_config.max_paths or path_tracker.result_count[0] < filter_config.max_paths:
        path_tracker.seen.add(tuple(field_info[:-1]))  # Exclude model_path from uniqueness check
        path_tracker.result_count[0] += 1
        return [list(field_info)]

    return []


def get_fields(
    Model: type[models.Model],
    parent_field: str = "",
    path_tracker: Optional[PathTracker] = None,
    filter_config: Optional[FilterConfig] = None,
    model_path: Optional[list[str]] = None,
) -> list[list[str]]:
    """Given a Model, return a list of lists with field info."""
    # Initialize configuration
    if isinstance(Model, basestring):
        Model = get_model_from_input(Model)
        if Model is None:
            return []

    path_tracker = path_tracker or PathTracker.create()
    filter_config = filter_config or FilterConfig(
        excludes=["permissions", "comment", "content_type"],
        max_depth=None,
        max_paths=None,
        field_type=None,
        target_model=None,
        target_field=None,
    )
    model_path = model_path or []

    # Early exit conditions
    if filter_config.max_paths and path_tracker.result_count[0] >= filter_config.max_paths:
        return []

    fields = Model._meta.fields + Model._meta.many_to_many + Model._meta.get_fields()
    path_tracker.model_stack.append(Model)

    # Check recursion limits
    if check_redundant(path_tracker.model_stack, path_tracker.stack_limit, filter_config.max_depth):
        return []

    out_fields = []
    for field in fields:
        # Process current field
        field_results = process_field(field, parent_field, Model, path_tracker, filter_config, model_path)
        out_fields.extend(field_results)

        # Continue traversing relations if needed
        if is_valid_instance(field) and (
            not filter_config.max_paths or path_tracker.result_count[0] < filter_config.max_paths
        ):

            RelModel = get_rel_model(field)
            full_field = get_full_field(parent_field, get_field_name(field))

            # Update model_path for the recursive call
            current_path = model_path + [Model._meta.label]

            # Skip traversal if the relationship should be excluded
            if not should_skip_field(full_field, RelModel.__name__, ",".join(current_path), filter_config.excludes):
                child_fields = get_fields(
                    RelModel,
                    full_field,
                    PathTracker(
                        seen=path_tracker.seen,
                        result_count=path_tracker.result_count,
                        model_stack=list(path_tracker.model_stack),
                        stack_limit=path_tracker.stack_limit,
                    ),
                    filter_config,
                    current_path,
                )
                out_fields.extend(child_fields)

    return out_fields


def get_ordered_fields(
    Model: ModelInput,
    by_depth: bool = False,
    by_model: bool = False,
    target_model: ModelInput = None,
    target_field: str = None,
    max_depth: int = None,
    max_paths: int = None,
    excludes: list[str] = None,
    field_type: str = None,
    **kwargs,
) -> list:
    """Get a list of fields from a model object, ordered by field name."""
    Model = get_model_from_input(Model)
    if Model is None:
        return []

    # Convert target_model if it's a string
    if isinstance(target_model, basestring):
        target_model = get_model_from_input(target_model)
        if target_model is None:
            return []

    filter_config = FilterConfig(
        excludes=excludes or ["permissions", "comment", "content_type"],
        max_depth=max_depth,
        max_paths=max_paths,
        field_type=field_type,
        target_model=target_model,
        target_field=target_field,
    )

    fields = get_fields(Model, filter_config=filter_config)

    if by_model:
        return sorted(fields, key=lambda x: x[1])
    if by_depth:
        return sorted(fields, key=lambda x: (x[0].count("__"), x[0]))
    return sorted(fields, key=lambda x: x[0])
