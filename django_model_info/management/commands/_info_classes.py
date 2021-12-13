from dataclasses import astuple, dataclass


@dataclass
class ModelInfo:
    """Class for keeping track of fields that are relations."""

    @dataclass
    class Annotated:
        title: str = ""
        value: str = ""

    model_name: Annotated = Annotated(title="Model Name", value="")
    verbose_name: str = Annotated(title="Verbose Name", value="")
    docstring: str = Annotated(title="Docstring", value="")
    is_abstract: str = Annotated(title="Is Abstract", value="")
    is_proxy: str = Annotated(title="Is Proxy", value="")
    is_managed: str = Annotated(title="Is Managed", value="")
    database_table: str = Annotated(title="Database Tables", value="")
    base_manager: str = Annotated(title="Base Manager", value="")
    default_manager: str = Annotated(title="Default Manager", value="")
    file: str = Annotated(title="File", value="")
    line_number: str = Annotated(title="Starting Line Number", value="")

    def render_rows(self, row_count: int) -> list:
        rows = []
        for row_num, entry in enumerate(self.__dataclass_fields__):
            if row_num <= row_count:
                field = getattr(self, entry)
                title = field.title
                value = field.value
                rows.append((title, value))
        return rows

    def render_simple_rows(self) -> list:
        """Renders a single row"""
        return [self.model_name.title, self.model_name.value]

    def __str__(self):
        return self.model_name.value


@dataclass
class BaseInfo:
    """Base class for keeping track of model fields and methods."""

    name: str = ""

    def render_row(self, column_count: int) -> list:
        return list(astuple(self))[:column_count]

    def render_simple_row(self) -> list:
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

    method_signature: str = ""
    method_docstring: str = ""
    method_file: str = ""
    method_line_number: str = ""
