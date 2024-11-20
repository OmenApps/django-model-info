"""Classes for keeping track of model fields and methods."""

from dataclasses import astuple, dataclass, field, fields


@dataclass
class Annotated:
    """Class for annotating model fields with title and value."""

    title: str = ""
    value: str = ""


@dataclass
class ModelInfo:
    """Class for keeping track of fields that are relations."""

    model_name: Annotated = field(default_factory=lambda: Annotated(title="Model Name"))
    verbose_name: Annotated = field(default_factory=lambda: Annotated(title="Verbose Name"))
    verbose_name_plural: Annotated = field(default_factory=lambda: Annotated(title="Verbose Name Plural"))
    docstring: Annotated = field(default_factory=lambda: Annotated(title="Docstring"))
    is_abstract: Annotated = field(default_factory=lambda: Annotated(title="Is Abstract"))
    is_proxy: Annotated = field(default_factory=lambda: Annotated(title="Is Proxy"))
    is_managed: Annotated = field(default_factory=lambda: Annotated(title="Is Managed"))
    ordering: Annotated = field(default_factory=lambda: Annotated(title="Ordering"))
    permissions: Annotated = field(default_factory=lambda: Annotated(title="Permissions"))
    default_permissions: Annotated = field(default_factory=lambda: Annotated(title="Default Permissions"))
    indexes: Annotated = field(default_factory=lambda: Annotated(title="Indexes"))
    constraints: Annotated = field(default_factory=lambda: Annotated(title="Constraints"))
    database_table: Annotated = field(default_factory=lambda: Annotated(title="Database Table"))
    database_table_comment: Annotated = field(default_factory=lambda: Annotated(title="Database Table Comment"))
    database_tablespace: Annotated = field(default_factory=lambda: Annotated(title="Database Tablespace"))
    base_manager: Annotated = field(default_factory=lambda: Annotated(title="Base Manager"))
    default_manager: Annotated = field(default_factory=lambda: Annotated(title="Default Manager"))
    file: Annotated = field(default_factory=lambda: Annotated(title="File"))
    line_number: Annotated = field(default_factory=lambda: Annotated(title="Starting Line Number"))
    mro: Annotated = field(default_factory=lambda: Annotated(title="Method Resolution Order"))
    base_manager: Annotated = field(default_factory=lambda: Annotated(title="Base Manager"))
    default_manager: Annotated = field(default_factory=lambda: Annotated(title="Default Manager"))
    managers_info: dict = field(default_factory=dict)  # Add this line

    def render_rows(self, row_count: int) -> list:
        """Renders multiple rows."""
        rows = []
        for row_num, field_info in enumerate(fields(self)):
            if row_num <= row_count:
                field_value = getattr(self, field_info.name)

                # Check if the field_value is an instance of Annotated
                if isinstance(field_value, Annotated):
                    title = field_value.title
                    value = field_value.value
                else:
                    # If it's not an Annotated instance, treat it as a string or another type
                    title = field_info.name.replace("_", " ").title()  # Generate title from field name
                    value = str(field_value)  # Convert to string in case it's not

                rows.append((title, value))
        return rows

    def __str__(self):
        return self.model_name.value


@dataclass
class BaseInfo:
    """Base class for keeping track of model fields and methods."""

    name: str = ""

    def render_row(self, column_count: int) -> list:
        """Renders a single row."""
        return list(astuple(self))[:column_count]

    def render_simple_row(self) -> list:
        """Renders a single simple row."""
        return [
            self.name,
        ]

    def __str__(self):
        return self.name


@dataclass
class FieldRelation(BaseInfo):
    """Class for keeping track of fields that are relations."""

    field_type: str = ""
    field_column: str = ""
    field_db_type: str = ""
    related_model: str = ""
    related_name: str = ""


@dataclass
class FieldReverseRelation(BaseInfo):
    """Class for keeping track of fields that are relations."""

    field_type: str = ""
    field_db_type: str = ""
    related_model: str = ""
    field_name_on_related_model: str = ""
    field_type_on_related_model: str = ""


@dataclass
class FieldOther(BaseInfo):
    """Class for keeping track of fields that are relations."""

    field_type: str = ""
    field_column: str = ""
    field_db_type: str = ""
    field_verbose_name: str = ""


@dataclass
class Method(BaseInfo):
    """Class for keeping track of dunder methods."""

    signature: str = ""
    docstring: str = ""
    file: str = ""
    line_number: str = ""
