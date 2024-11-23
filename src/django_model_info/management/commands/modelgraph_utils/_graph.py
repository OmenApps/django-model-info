"""Graph building utilities for model relationships."""
from datetime import timedelta
from typing import TypeVar

import networkx as nx
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
ModelInput = type[models.Model] | str
basestring = (str, bytes)


def get_relationship_type(field) -> str:
    """Get the relationship type for a field."""
    if field.__class__.__name__ == "OneToOneField":
        return "OneToOneField"
    elif field.__class__.__name__ == "ForeignKey":
        return "ForeignKey"
    elif field.__class__.__name__ == "ManyToManyField":
        return "ManyToManyField"
    elif field.__class__.__name__ == "OneToOneRel":
        return "OneToOneRel"
    elif field.__class__.__name__ == "ManyToOneRel":
        return "ManyToOneRel"
    elif field.__class__.__name__ == "ManyToManyRel":
        return "ManyToManyRel"
    return "Unknown"


def get_model_from_input(model_input) -> type[models.Model]:
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


# Check the get_model_from_input() from modelfilters


def get_model_list(filter_option=None, prefix=None, exclude=None, abstract=None, proxy=None) -> list:
    """Get filtered list of models based on various criteria."""
    models = []

    # Get initial model list
    if not filter_option:
        models = apps.get_models(include_auto_created=True)
    else:
        for filter_item in filter_option:
            if "." in filter_item:
                try:
                    model = apps.get_model(filter_item)
                    models.append(model)
                except LookupError:
                    continue
            else:
                try:
                    app_models = apps.get_app_config(filter_item).get_models(
                        include_auto_created=True,
                    )
                    models.extend(app_models)
                except LookupError:
                    # Try to find models that match the name
                    matching_models = [
                        m for m in apps.get_models(include_auto_created=True) if m.__name__ == filter_item
                    ]
                    models.extend(matching_models)

    # Apply filters
    filtered_models = []
    for model in models:
        # Skip if model should be excluded
        if exclude and (
            model.__name__ in exclude
            or f"{model._meta.app_label}.{model.__name__}" in exclude
            or model._meta.app_label in exclude
        ):
            continue

        # Skip if model doesn't match prefix
        if prefix and not model.__name__.startswith(prefix):
            continue

        # Handle abstract models
        if model._meta.abstract and not abstract:
            continue

        # Handle proxy models
        if model._meta.proxy and not proxy:
            continue

        filtered_models.append(model)

    return sorted(filtered_models, key=lambda x: (x._meta.app_label, x._meta.object_name))


def build_modelgraph(model_list: list) -> nx.MultiDiGraph:
    """Build graph representing model relationships."""
    G = nx.MultiDiGraph()

    model_labels = {f"{model._meta.app_label}.{model._meta.model_name}" for model in model_list}

    # Add nodes
    for model in model_list:
        model_label = f"{model._meta.app_label}.{model._meta.model_name}"
        G.add_node(model_label, model=model)

    # Add edges
    for model in model_list:
        model_label = f"{model._meta.app_label}.{model._meta.model_name}"
        fields = model._meta.get_fields(include_hidden=True)

        for field in fields:
            if hasattr(field, "related_model") and field.related_model:
                related_label = f"{field.related_model._meta.app_label}." f"{field.related_model._meta.model_name}"

                if related_label in model_labels:
                    relationship_type = get_relationship_type(field)
                    direction = (
                        "forward"
                        if relationship_type in ("OneToOneField", "ForeignKey", "ManyToManyField")
                        else "reverse"
                    )

                    G.add_edge(
                        model_label,
                        related_label,
                        key=direction,
                        relationship_type=relationship_type,
                        field_name=field.name,
                        direction=direction,
                    )

    return G
