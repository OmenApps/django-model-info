"""Provides a management command to list out the fields and methods for each model in a Django project."""

import inspect
from pathlib import Path
from typing import List, Optional
from django.apps import apps as django_apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser, DjangoHelpFormatter
from rich.align import Align
from rich.bar import Bar
from rich.console import Console
from rich.padding import Padding
from rich.style import Style
from rich.table import Table

from ._field_attr_utils import (
    get_field_column,
    get_field_db_type,
    get_field_name,
    get_field_name_on_reverse_model,
    get_field_type,
    get_field_type_on_reverse_model,
    get_field_verbose_name,
    get_related_model,
    get_related_name,
)
from ._info_classes import FieldOther, FieldRelation, FieldReverseRelation, Method, ModelInfo
from ._method_attr_utils import get_method_docstring, get_method_file, get_method_line_number, get_method_signature
from ._model_attr_utils import (
    get_model_base_manager,
    get_model_constraints,
    get_model_database_table,
    get_model_database_table_comment,
    get_model_database_tablespace,
    get_model_default_manager,
    get_model_default_permissions,
    get_model_docstring,
    get_model_file,
    get_model_indexes,
    get_model_is_abstract,
    get_model_is_managed,
    get_model_is_proxy,
    get_model_line_number,
    get_model_mro,
    get_model_name,
    get_model_ordering,
    get_model_permissions,
    get_model_verbose_name,
    get_model_verbose_name_plural,
)

SECTION_STYLE = Style(color="green", bold=True, underline=True)
SUBSECTION_STYLE = Style(color="green", bold=True)

COMMON_DJANGO_FIELDS = {  # ToDo: Add a setting to allow skipping these when only showing user-added fields
    # "id",
    # "something_else",
}

DEFAULT_DJANGO_METHODS = (
    "_check_column_name_clashes",
    "_check_constraints",
    "_check_db_table_comment",
    "_check_default_pk",
    "_check_field_name_clashes",
    "_check_fields",
    "_check_id_field",
    "_check_index_together",
    "_check_indexes",
    "_check_local_fields",
    "_check_long_column_names",
    "_check_m2m_through_same_relationship",
    "_check_managers",
    "_check_model",
    "_check_model_name_db_lookup_clashes",
    "_check_ordering",
    "_check_property_name_related_field_accessor_clashes",
    "_check_single_primary_key",
    "_check_swappable",
    "_check_unique_together",
    "_do_insert",
    "_do_update",
    "_get_expr_references",
    "_get_FIELD_display",
    "_get_field_expression_map",
    "_get_next_or_previous_by_FIELD",
    "_get_next_or_previous_in_order",
    "_get_pk_val",
    "_get_unique_checks",
    "_meta",
    "_parse_params",
    "_perform_date_checks",
    "_perform_unique_checks",
    "_prepare_related_fields_for_save",
    "_save_parents",
    "_save_table",
    "_set_pk_val",
    "_validate_force_insert",
    "adelete",
    "arefresh_from_db",
    "asave",
    "check",
    "clean",
    "clean_fields",
    "date_error_message",
    "delete",
    "from_db",
    "full_clean",
    "get_absolute_url",
    "get_constraints",
    "get_decoded",
    "get_deferred_fields",
    "get_next_by_expire_date",
    "get_previous_by_expire_date",
    "get_session_store_class",
    "prepare_database_save",
    "refresh_from_db",
    "save",
    "save_base",
    "serializable_value",
    "unique_error_message",
    "validate_constraints",
    "validate_unique",
)

console = Console(record=True)


def clean_docstring(text: str) -> str:
    """Clean docstring by preserving code blocks and handling line breaks."""
    if not text:
        return ""

    # Escape code blocks
    text = text.replace("```", "\\```")
    # Replace line breaks with HTML tags
    text = text.replace("\n\n", "</p><p>").replace("\n", "<br>")
    # Escape markdown characters
    text = text.replace("_", "\\_").replace("*", "\\*")
    text = text.replace("|", "\\|")
    # Wrap non-code content in p tags if not already wrapped
    if not text.startswith("<p>"):
        text = f"<p>{text}</p>"
    return text


class ModelProcessor:
    """Process a model to extract model information, fields, and methods."""

    def __init__(self, model, verbosity_option, exclude_defaults, markdown=False):
        self.model = model
        self.verbosity_option = verbosity_option
        self.exclude_defaults = exclude_defaults
        self.markdown = markdown

    def build_model_info(self):
        """Return the essential details of the model."""
        new_model = ModelInfo()
        new_model.model_name.value = get_model_name(self.model)
        new_model.verbose_name.value = get_model_verbose_name(self.model)
        new_model.verbose_name_plural.value = get_model_verbose_name_plural(self.model)
        new_model.docstring.value = (
            clean_docstring(get_model_docstring(self.model)) if self.markdown else get_model_docstring(self.model)
        )
        new_model.is_abstract.value = get_model_is_abstract(self.model)
        new_model.is_proxy.value = get_model_is_proxy(self.model)
        new_model.is_managed.value = get_model_is_managed(self.model)
        new_model.ordering.value = get_model_ordering(self.model)
        new_model.permissions.value = get_model_permissions(self.model)
        new_model.default_permissions.value = get_model_default_permissions(self.model)
        new_model.indexes.value = get_model_indexes(self.model)
        new_model.constraints.value = get_model_constraints(self.model)
        new_model.database_table.value = get_model_database_table(self.model)
        new_model.database_tablespace.value = get_model_database_tablespace(self.model)
        new_model.database_table_comment.value = get_model_database_table_comment(self.model)
        new_model.base_manager.value = get_model_base_manager(self.model)
        new_model.default_manager.value = get_model_default_manager(self.model)
        new_model.file.value = get_model_file(self.model)
        new_model.line_number.value = get_model_line_number(self.model)
        new_model.mro.value = get_model_mro(self.model)

        return new_model

    def build_relation_field_info(self):
        """Process and categorize fields into relations."""
        field_list = self.model._meta.get_fields(include_hidden=True)  # pylint: disable=W0212
        fields_relation = []

        for field in field_list:
            if hasattr(field, "related_model") and field.related_model is not None:
                if "reverse_related" not in str(field.__class__.__module__):
                    fields_relation.append(self.build_relation_field(field))

        return fields_relation

    def build_reverse_relation_field_info(self):
        """Process and categorize fields into reverse relations."""
        field_list = self.model._meta.get_fields(include_hidden=True)  # pylint: disable=W0212
        fields_reverse_relation = []

        for field in field_list:
            if hasattr(field, "related_model") and field.related_model is not None:
                if "reverse_related" in str(field.__class__.__module__):
                    fields_reverse_relation.append(self.build_reverse_relation_field(field))

        return fields_reverse_relation

    def build_other_field_info(self):
        """Process and categorize fields into others."""
        field_list = self.model._meta.get_fields(include_hidden=True)  # pylint: disable=W0212
        fields_other = []

        for field in field_list:
            if (
                getattr(field, "related_model", None) is None
                and (not self.exclude_defaults, False)
                or field.name not in COMMON_DJANGO_FIELDS
            ):
                fields_other.append(self.build_other_field(field))

        return fields_other

    def build_relation_field(self, field):
        """Build a relation field."""
        model_is_abstract = self.model._meta.abstract  # pylint: disable=W0212
        return FieldRelation(
            name=get_field_name(field),
            field_type=get_field_type(field),
            field_column=get_field_column(field),
            field_db_type=get_field_db_type(field) if not model_is_abstract else "Not applicable",
            related_model=get_related_model(field) if not model_is_abstract else "Not applicable",
            related_name=get_related_name(field, self.model) if not model_is_abstract else "Not applicable",
        )

    def build_reverse_relation_field(self, field):
        """Build a reverse relation field."""
        return FieldReverseRelation(
            name=get_related_name(field, self.model),
            field_type=get_field_type(field),
            field_db_type=get_field_db_type(field),
            related_model=get_related_model(field),
            field_name_on_related_model=get_field_name_on_reverse_model(field),
            field_type_on_related_model=get_field_type_on_reverse_model(field),
        )

    def build_other_field(self, field):
        """Build a field that is not a relation."""
        return FieldOther(
            name=get_field_name(field),
            field_type=get_field_type(field),
            field_column=get_field_column(field),
            field_db_type=get_field_db_type(field),
            field_verbose_name=get_field_verbose_name(field),
        )

    def build_method_info(self, method_list: List):
        """Categorize methods into dunder, common Django, private, and other."""
        method_dunder, method_common_django, method_other_private, method_other = [], [], [], []

        for method_name in method_list:
            new_method = self.build_method(method_name)
            if method_name.startswith("__") and method_name.endswith("__"):
                method_dunder.append(new_method)
            elif method_name in DEFAULT_DJANGO_METHODS:
                method_common_django.append(new_method)
            elif method_name.startswith("_"):
                method_other_private.append(new_method)
            else:
                method_other.append(new_method)
        if not self.exclude_defaults:
            return method_dunder, method_common_django, method_other_private, method_other
        return method_other_private, method_other

    def build_method(self, method_name: str):
        """Build a method's information."""
        method = Method(name=method_name)
        if self.verbosity_option > 1:
            method.signature = get_method_signature(method_name, self.model, self.verbosity_option)
        if self.verbosity_option > 2:
            method.docstring = get_method_docstring(method_name, self.model)
            method.file = get_method_file(method_name, self.model)
            method.line_number = get_method_line_number(method_name, self.model)
        return method


class Command(BaseCommand):
    """A Django management command to list out the fields and methods for each model."""

    help = "List out the fields and methods for each model"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verbosity = 2
        self.filter_option = None
        self.export_option = None
        self.model_list = []

    def create_parser(self, prog_name: str, subcommand: str, **kwargs):
        """Create and return the ``ArgumentParser`` which will be used to parse the arguments to this command.

        Reimplemented to allow new default verbosity of 2.
        """
        parser = CommandParser(
            prog=f"{Path(prog_name)} {subcommand}",
            description=self.help or None,
            formatter_class=DjangoHelpFormatter,
            missing_args_message=getattr(self, "missing_args_message", None),
            called_from_command_line=getattr(self, "_called_from_command_line", None),
            **kwargs,
        )
        parser.add_argument("--version", action="version", version=self.get_version())
        parser.add_argument(
            "--settings",
            help=(
                "The Python path to a settings module, e.g. "
                '"myproject.settings.main". If this isn\'t provided, the '
                "DJANGO_SETTINGS_MODULE environment variable will be used."
            ),
        )
        parser.add_argument(
            "--pythonpath",
            help='A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".',
        )
        parser.add_argument("--traceback", action="store_true", help="Raise on CommandError exceptions")
        parser.add_argument(
            "--no-color",
            action="store_true",
            help="Don't colorize the command output.",
        )
        parser.add_argument(
            "--force-color",
            action="store_true",
            help="Force colorization of the command output.",
        )
        if self.requires_system_checks:
            parser.add_argument(
                "--skip-checks",
                action="store_true",
                help="Skip system checks.",
            )
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser: CommandParser):
        """Add custom arguments to the command."""
        super().add_arguments(parser)
        parser.add_argument(
            "-v",
            "--verbosity",
            default=2,
            type=int,
            choices=[0, 1, 2, 3],
            help="Verbosity level: "
            "0 Model names only - Convenient when you just need a list of all your project's models in one place, "
            "1 Model names + field names +non-dunder/common method names, "
            "2 (default) Model names + field names & details + non-dunder/common method names & details, "
            "3 Model names + field names & details + all method names & details.",
        )
        parser.add_argument(
            "--exclude-defaults",
            action="store_true",
            help="Show only user-defined fields and methods, skipping Django's default fields and methods.",
        )
        parser.add_argument(
            "-e",
            "--export",
            nargs="?",
            type=str,
            default=None,
            help="Filename to export. Extension must be .txt, .html, .htm, or .md",
        )
        parser.add_argument(
            "-m",
            "--markdown",
            action="store_true",
            help="Output in markdown format to the console",
        )
        parser.add_argument(
            "-f",
            "--filter",
            nargs="+",
            type=str,
            default=None,
            help="Provide one or more apps or models, to which the results will be limited. "
            "Input should be in the form `appname` or `appname.Modelname`.",
        )

    def get_options(self, options) -> tuple:
        """Get verbosity, filter, and export options."""
        verbosity = options.get("verbosity", None)
        if verbosity is None:
            verbosity = (
                getattr(settings, "MODEL_INFO_VERBOSITY", 2)
                if isinstance(getattr(settings, "MODEL_INFO_VERBOSITY", 2), int)
                else 2
            )

        filter_option = options.get("filter", None)
        if filter_option is None:
            filter_option = (
                getattr(settings, "MODEL_INFO_FILTER", None)
                if isinstance(getattr(settings, "MODEL_INFO_FILTER", None), list)
                else None
            )
        export_option = (
            options.get("export")
            if options.get("export", None) is not None and isinstance(options.get("export"), str)
            else None
        )
        exclude_defaults = options.get("exclude_defaults", False)

        return verbosity, filter_option, export_option, exclude_defaults

    def handle(self, *_, **options):
        """Handle the command."""
        self.verbosity, self.filter_option, self.export_option, self.exclude_defaults = self.get_options(options)
        self.markdown = options.get("markdown", False)

        self.model_list = self.get_model_list()

        if self.markdown:
            # Print markdown directly to console
            print(self.export_markdown())
            return

        for model in self.model_list:
            if self.verbosity > 0:
                console.print(Padding("", (1, 0, 0, 0)))
                console.print(Padding("", (0, 0, 0, 0), style=SECTION_STYLE))
                console.print(Padding("", (0, 0, 0, 0)))
            console.print(f"{model._meta.label}", style=SECTION_STYLE)  # pylint: disable=W0212

            if self.verbosity > 0:
                processor = ModelProcessor(model, self.verbosity, self.exclude_defaults, markdown=False)
                model_info = processor.build_model_info()
                self.render_model_info(model_info)

                fields_other = processor.build_other_field_info()
                self.render_other_fields(fields_other)

                fields_relation = processor.build_relation_field_info()
                self.render_relation_fields(fields_relation)

                if not model._meta.abstract:  # pylint: disable=W0212
                    fields_reverse_relation = processor.build_reverse_relation_field_info()
                    self.render_reverse_relation_fields(fields_reverse_relation)

                method_list = self.get_clean_method_list(model)
                method_info = processor.build_method_info(method_list)
                self.render_methods(method_info)

        console.print(f"\nTotal Models Listed: {len(self.model_list)}\n", style=SECTION_STYLE)
        console.print(Align(Bar(size=0.1, begin=0.0, end=0.0, width=100), align="center"), style="red")

        if self.export_option:
            self.export_results()

    def get_model_list(self):
        """Retrieve models based on filter option or return all models."""
        if self.filter_option:
            return self.filter_models()
        return sorted(
            django_apps.get_models(), key=lambda x: (x._meta.app_label, x._meta.object_name)  # pylint: disable=W0212
        )

    def append_abstract_models(self):
        """Retrieve abstract models.

        For each model in the model list, we get MRO, and add any class in the MRO that is in the same app as the model.
        """
        abstract_models = []
        for model in self.model_list:
            mro = inspect.getmro(model)
            for item in mro:
                try:
                    if item._meta.app_label == model._meta.app_label:  # pylint: disable=W0212
                        abstract_models.append(item)
                except AttributeError:
                    pass
        return abstract_models

    def filter_models(self):
        """Get the list of filtered models based on user input."""
        model_list = []
        for filter_item in self.filter_option:
            if "." in filter_item:
                model = django_apps.get_model(filter_item)
                model_list.append(model)
            else:
                try:
                    app_models = list(django_apps.get_app_config(filter_item).get_models())
                    model_list.extend(app_models)
                except LookupError:
                    pass
        abstract_models = self.append_abstract_models()
        if abstract_models:
            model_list.extend(abstract_models)
        return model_list

    def render_model_info(self, model_info):
        """Render model information."""
        table = Table(title="Model Info")

        row_count = 3
        if self.verbosity > 1:
            row_count = 5
        if self.verbosity > 2:
            row_count = 19

        table.add_column("Key", justify="left", style="blue")
        table.add_column("Value", justify="left", style="magenta")

        if isinstance(model_info, ModelInfo):
            for row in model_info.render_rows(row_count):
                new_row = tuple(row)
                table.add_row(new_row[0], new_row[1])

        else:
            table.add_row("none")

        console.print(Padding(table, (1, 0, 0, 8)))

    def render_field_relations_table(self, title, data_list):
        """Render table for field relations."""

        table = Table(title=title)
        column_count = 1

        table.add_column("Field Name", justify="left", style="yellow", no_wrap=True)
        if self.verbosity >= 2:
            column_count = 6
            table.add_column("Field Type", justify="left", style="magenta")
            table.add_column("Database Column", justify="left", style="magenta")
            table.add_column("Database Type", justify="left", style="magenta")
            table.add_column("Related Model", justify="right", style="dark_red")
            table.add_column("Related Name", justify="right", style="dark_red")

        field_table = self._fill_table(table, data_list, FieldRelation, column_count)
        self._render_table(field_table)

    def render_field_reverse_relations_table(self, title, data_list):
        """Render table for field reverse relations."""
        table = Table(title=title)
        column_count = 1

        table.add_column("Field Name", justify="left", style="yellow", no_wrap=True)
        if self.verbosity >= 2:
            column_count = 7
            table.add_column("Field Type", justify="left", style="magenta")
            table.add_column("Database Type", justify="left", style="magenta")
            table.add_column("Related Model", justify="right", style="dark_red")
            table.add_column("Field Name on Related Model", justify="left", style="dark_red")
            table.add_column("Field Type on Related Model", justify="left", style="dark_red")

        field_table = self._fill_table(table, data_list, FieldReverseRelation, column_count)
        self._render_table(field_table)

    def render_field_other_table(self, title, data_list):
        """Render table for other fields."""
        table = Table(title=title)
        column_count = 1

        table.add_column("Field Name", justify="left", style="yellow", no_wrap=True)
        if self.verbosity >= 2:
            column_count = 6
            table.add_column("Field Type", justify="left", style="magenta")
            table.add_column("Database Column", justify="left", style="magenta")
            table.add_column("Database Type", justify="left", style="magenta")
            table.add_column("Verbose Name", justify="left", style="white")

        field_table = self._fill_table(table, data_list, FieldOther, column_count)
        self._render_table(field_table)

    def render_other_fields(self, fields_other):
        """Render tables for fields."""
        console.print(Padding("Fields:", (1, 0, 0, 4), style=SUBSECTION_STYLE))

        self.render_field_other_table("Other Fields", fields_other)

    def render_relation_fields(self, fields_relation):
        """Render tables for fields."""
        self.render_field_relations_table("Relations", fields_relation)

    def render_reverse_relation_fields(self, fields_reverse_relation):
        """Render tables for fields."""
        self.render_field_reverse_relations_table("Reverse Relations", fields_reverse_relation)

    def render_method_table(self, title, data_list):
        """Render table for methods."""
        table = Table(title=title)
        column_count = 1

        table.add_column("Method Name", justify="left", style="yellow", no_wrap=True)
        if self.verbosity >= 2:
            column_count = 2
            table.add_column("Signature", justify="left", style="magenta")
        if self.verbosity >= 3:
            column_count = 5
            table.add_column("Docstring", justify="left", style="magenta")
            table.add_column("File", justify="left", style="magenta")
            table.add_column("Line Number", justify="left", style="magenta")

        method_table = self._fill_table(table, data_list, Method, column_count)
        self._render_table(method_table)

    def render_methods(self, method_info):
        """Render tables for methods."""
        if self.verbosity == 3:
            console.print(Padding("Methods (all):", (1, 0, 0, 4), style=SUBSECTION_STYLE))
        else:
            console.print(Padding("Methods (non-private/internal):", (1, 0, 0, 4), style=SUBSECTION_STYLE))

        if self.exclude_defaults:
            method_other_private, method_other = method_info
        else:
            method_dunder, method_common_django, method_other_private, method_other = method_info

        if not self.exclude_defaults:
            if self.verbosity > 1:
                self.render_method_table("Dunder Methods", method_dunder)
                self.render_method_table("Common Django Methods", method_common_django)
        self.render_method_table("Private Methods", method_other_private)
        self.render_method_table("Other Methods", method_other)

    def _fill_table(self, table: Table, info_object_list: Optional[List], info_type: type, column_count: int):
        """Given a rich table, a list of info objects, and the type of info object, fill the table."""
        if isinstance(info_object_list, list) and all(isinstance(row, info_type) for row in info_object_list):
            sorted_field_object_list = sorted(info_object_list, key=lambda x: x.name)
            for row in sorted_field_object_list:
                if self.verbosity >= 2:
                    table.add_row(*row.render_row(column_count=column_count))
                else:
                    table.add_row(*row.render_simple_row())
        else:
            table.add_row("none")

        return table

    def _render_table(self, table):
        """Helper method to print table based on data."""
        console.print(Padding(table, (1, 0, 0, 8)))

    def export_markdown(self) -> str:
        """Generate markdown output with tables."""
        md_output = []

        for model in self.model_list:
            md_output.append(f"# {model._meta.label}\n")
            processor = ModelProcessor(model, self.verbosity, self.exclude_defaults, markdown=True)

            # Model Info section
            md_output.append("## Model Info\n")
            info_table = ["| Key | Value |", "|-----|-------|"]
            model_info = processor.build_model_info()
            for row in model_info.render_rows(19):
                if row[1]:
                    info_table.append(f"| {row[0]} | {row[1]} |")
            md_output.extend(info_table)
            md_output.append("\n")

            if self.verbosity > 0:
                # Other Fields section
                fields_other = processor.build_other_field_info()
                if fields_other:
                    md_output.append("## Fields\n")
                    headers = ["| Field Name | Field Type | Database Column | Database Type | Verbose Name |"]
                    separator = ["|------------|------------|----------------|---------------|--------------|"]
                    if self.verbosity < 2:
                        headers = ["| Field Name |"]
                        separator = ["|------------|"]
                    md_output.append("".join(headers))
                    md_output.append("".join(separator))

                    for field in sorted(fields_other, key=lambda x: x.name):
                        if self.verbosity >= 2:
                            row = [
                                f"| `{field.name}`",
                                field.field_type,
                                field.field_column,
                                field.field_db_type,
                                f"{field.field_verbose_name} |",
                            ]
                        else:
                            row = [f"| `{field.name}` |"]
                        md_output.append(" | ".join(row))
                    md_output.append("\n")

                # Relations section
                fields_relation = processor.build_relation_field_info()
                if fields_relation:
                    md_output.append("## Relations\n")
                    headers = [
                        "| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |"
                    ]
                    separator = [
                        "|------------|------------|----------------|---------------|---------------|--------------|"
                    ]
                    if self.verbosity < 2:
                        headers = ["| Field Name |"]
                        separator = ["|------------|"]
                    md_output.append("".join(headers))
                    md_output.append("".join(separator))

                    for field in sorted(fields_relation, key=lambda x: x.name):
                        if self.verbosity >= 2:
                            row = [
                                f"| `{field.name}`",
                                field.field_type,
                                field.field_column,
                                field.field_db_type,
                                field.related_model,
                                f"{field.related_name} |",
                            ]
                        else:
                            row = [f"| `{field.name}` |"]
                        md_output.append(" | ".join(row))
                    md_output.append("\n")

                # Methods section
                method_list = self.get_clean_method_list(model)
                methods = processor.build_method_info(method_list)

                if any(methods):
                    md_output.append("## Methods\n")
                    if self.exclude_defaults:
                        method_types = ["Private", "Other"]
                    else:
                        method_types = ["Dunder", "Common Django", "Private", "Other"]
                    for method_type, method_list in zip(method_types, methods):
                        if method_list:
                            md_output.append(f"### {method_type} Methods\n")
                            headers = ["| Method Name |"]
                            separator = ["|-------------|"]
                            if self.verbosity >= 2:
                                headers.extend(["Signature |"])
                                separator.extend(["----------|"])
                            if self.verbosity >= 3:
                                headers.extend(["Docstring", "File", "Line Number |"])
                                separator.extend(["---------", "----", "------------|"])
                            md_output.append("".join(headers))
                            md_output.append("".join(separator))

                            for method in sorted(method_list, key=lambda x: x.name):
                                row = [f"| `{method.name}`"]
                                if self.verbosity >= 2:
                                    row.append(f"`{method.signature}`" if method.signature else "")
                                if self.verbosity >= 3:
                                    row.extend(
                                        [
                                            clean_docstring(method.docstring) if method.docstring else "",
                                            method.file if method.file else "",
                                            f"{method.line_number} |" if method.line_number else " |",
                                        ]
                                    )
                                else:
                                    row[-1] += " |"
                                md_output.append(" | ".join(row))
                            md_output.append("\n")

            md_output.append("---\n")

        return "\n".join(md_output)

    def get_clean_method_list(self, model):
        """Clean method list by removing uppercase and non-callable methods."""
        return [
            method_name
            for method_name in dir(model)
            if method_name is not None
            and not method_name == ""
            and not method_name[0].isupper()
            and hasattr(model, method_name)
            and callable(getattr(model, method_name))
        ]

    def export_results(self):
        """Handle export functionality."""
        extension = Path(self.export_option).suffix
        if extension in [".html", ".htm"]:
            console.save_html(path=self.export_option)
        elif extension == ".txt":
            console.save_text(path=self.export_option)
        elif extension == ".md":
            md_content = self.export_markdown()
            with open(self.export_option, "w", encoding="utf-8") as f:
                f.write(md_content)
