import os
from pathlib import Path

from django.apps import apps as django_apps
from django.core.management.base import BaseCommand, CommandParser, DjangoHelpFormatter
from django.db.models import Model
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
    get_model_database_table,
    get_model_default_manager,
    get_model_docstring,
    get_model_file,
    get_model_is_abstract,
    get_model_is_managed,
    get_model_is_proxy,
    get_model_line_number,
    get_model_name,
    get_model_verbose_name,
)

console = Console(record=True)


DEFAULT_DJANGO_METHODS = (
    "_check_column_name_clashes",
    "_check_constraints",
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
    "_get_next_or_previous_by_FIELD",
    "_get_next_or_previous_in_order",
    "_get_pk_val",
    "_get_unique_checks",
    "_meta",
    "_perform_date_checks",
    "_perform_unique_checks",
    "_prepare_related_fields_for_save",
    "_save_parents",
    "_save_table",
    "_set_pk_val",
    "check",
    "clean",
    "clean_fields",
    "date_error_message",
    "delete",
    "from_db",
    "full_clean",
    "get_absolute_url",
    "get_deferred_fields",
    "prepare_database_save",
    "refresh_from_db",
    "save",
    "save_base",
    "serializable_value",
    "unique_error_message",
    "validate_unique",
)


class Command(BaseCommand):
    """
    A management command which lists models within your project, and optionally, details about model fields and methods

    Verbosity outputs:
        0   Model names only
        1   Model names, field names, and non-dunder/common method names
        2 * Model names, field names & details, and non-dunder/common method names & details
        3   Model names, field names & details, and all method names & full details

        * Verbosity of 2 is default
    """

    help = "List out the fields and methods for each model"

    def create_parser(self, prog_name, subcommand, **kwargs):
        """
        Create and return the ``ArgumentParser`` which will be used to
        parse the arguments to this command.

        Reimplemented to allow new verbosity default
        """
        parser = CommandParser(
            prog="%s %s" % (os.path.basename(prog_name), subcommand),
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

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "-v",
            "--verbosity",
            default=2,
            type=int,
            choices=[0, 1, 2, 3],
            help="Verbosity level: "
            "0 Model names only, "
            "1 Model names + field names +non-dunder/common method names, "
            "2 (default) Model names + field names & details + non-dunder/common method names & details, "
            "3 Model names + field names & details + all method names & details.",
        )
        parser.add_argument(
            "--filename",
            nargs="?",
            type=str,
            default=None,
            help="Filename to save output to (optional). If provided, "
            "must have a file extension of `.txt`, `.html`, or `htm`",
        )
        parser.add_argument(
            "--model",
            nargs="?",
            type=str,
            default=None,
            help="list the details for a single model. Input should be in the form `appname.Modelname`",
        )

    def model_info(self, options):
        section_style = Style(color="green", bold=True, underline=True)
        subsection_style = Style(color="green", bold=True)

        VERBOSITY = options["verbosity"]
        MODEL = options.get("model", None)
        FILENAME = options.get("filename", None)

        def build_model_objects(model) -> ModelInfo:
            """
            Given a model, returns a ModelInfo object
            """

            new_model = ModelInfo()
            new_model.model_name.value = get_model_name(model)
            new_model.verbose_name.value = get_model_verbose_name(model)
            new_model.docstring.value = get_model_docstring(model)
            new_model.is_abstract.value = get_model_is_abstract(model)
            new_model.is_proxy.value = get_model_is_proxy(model)
            new_model.is_managed.value = get_model_is_managed(model)
            new_model.database_table.value = get_model_database_table(model)
            new_model.base_manager.value = get_model_base_manager(model)
            new_model.default_manager.value = get_model_default_manager(model)
            new_model.file.value = get_model_file(model)
            new_model.line_number.value = get_model_line_number(model)

            return new_model

        def build_field_objects(field_list: list) -> tuple:
            """
            Given a list of model fields, returns a tuple of FieldRelation,
            FieldReverseRelation, and FieldOther object lists
            """
            fields_relation = []
            fields_reverse_relation = []
            fields_other = []

            for field in field_list:
                # Identify the kind of field this is, and build associated object

                if hasattr(field, "related_model") and field.related_model is not None:
                    if "reverse_related" in field.__class__.__module__.__str__():
                        # Build a FieldReverseRelation object
                        new_field = FieldReverseRelation()
                        new_field.name = get_related_name(field)
                        new_field.field_type = get_field_type(field)
                        new_field.field_db_type = get_field_db_type(field)
                        new_field.related_model = get_related_model(field)
                        new_field.field_name_on_related_model = get_field_name_on_reverse_model(field)
                        new_field.field_type_on_related_model = get_field_type_on_reverse_model(field)

                        fields_reverse_relation.append(new_field)
                    else:
                        # Build a FieldRelation object
                        new_field = FieldRelation()
                        new_field.name = get_field_name(field)
                        new_field.field_type = get_field_type(field)
                        new_field.field_column = get_field_column(field)
                        new_field.field_db_type = get_field_db_type(field)
                        new_field.related_model = get_related_model(field)
                        new_field.related_name = get_related_name(field)

                        fields_relation.append(new_field)
                else:
                    # Build a FieldOther object
                    new_field = FieldOther()
                    new_field.name = get_field_name(field)
                    new_field.field_type = get_field_type(field)
                    new_field.field_column = get_field_column(field)
                    new_field.field_db_type = get_field_db_type(field)
                    new_field.field_verbose_name = get_field_verbose_name(field)

                    fields_other.append(new_field)

            return (
                fields_relation,
                fields_reverse_relation,
                fields_other,
            )

        def build_method_objects(method_list: list, model: Model) -> tuple:
            """
            Given a list of model methods, returns a tuple of MethodCommonDjango,
            MethodDunder, MethodOther, MethodOtherPrivate object lists
            """

            method_dunder = []
            method_common_django = []
            method_other_private = []
            method_other = []

            for method in method_list:
                # Build the object, and assign to the correct list
                new_method = Method()

                new_method.name = method
                if VERBOSITY > 1:
                    new_method.method_signature = get_method_signature(method, model, VERBOSITY)
                if VERBOSITY > 2:
                    new_method.method_docstring = get_method_docstring(method, model)
                    new_method.method_file = get_method_file(method, model)
                    new_method.method_line_number = get_method_line_number(method, model)

                if method.startswith("__") and method.endswith("__"):
                    # Dunder methods
                    method_dunder.append(new_method)

                elif method in DEFAULT_DJANGO_METHODS:
                    # Common Django methods
                    method_common_django.append(new_method)

                elif method.startswith("_"):
                    # Other Private methods
                    method_other_private.append(new_method)

                else:
                    # Other methods
                    method_other.append(new_method)

            return (
                method_dunder,
                method_common_django,
                method_other_private,
                method_other,
            )

        def _fill_table(info_table: Table, info_object_list: list or None, info_type: type, column_count: int):
            """
            Given a rich table, a list of
            """
            if isinstance(info_object_list, list) and all(isinstance(row, info_type) for row in info_object_list):
                sorted_field_object_list = sorted(info_object_list, key=lambda x: x.name)
                for row in sorted_field_object_list:

                    if VERBOSITY >= 2:
                        info_table.add_row(*row.render_row(column_count=column_count))
                    else:
                        info_table.add_row(*row.render_simple_row())

            else:
                info_table.add_row("none")

            return info_table

        def _print_table(table):
            console.print(Padding(table, (1, 0, 0, 8)))

        def render_model_table(info_object_list: list or None, info_type: type):
            """Provided a list of FieldRelation objects, prints the resulting sorted table to console"""
            model_table = Table(title="Model Details")
            row_count = 2
            if VERBOSITY > 1:
                row_count = 5
            if VERBOSITY > 2:
                row_count = 11

            model_table.add_column("Key", justify="left", style="blue", no_wrap=True)
            model_table.add_column("Value", justify="left", style="magenta")

            if isinstance(info_object_list, ModelInfo):
                for row in info_object_list.render_rows(row_count):
                    new_row = tuple(row)
                    model_table.add_row(new_row[0], new_row[1])

            else:
                model_table.add_row("none")

            _print_table(model_table)

        def render_field_relations_table(info_object_list: list or None, info_type: type):
            """Provided a list of FieldRelation objects, prints the resulting sorted table to console"""
            field_table = Table(title="Relations")
            column_count = 1

            field_table.add_column("Field Name", justify="left", style="yellow", no_wrap=True)
            if VERBOSITY >= 2:
                column_count = 6
                field_table.add_column("Field Type", justify="left", style="magenta")
                field_table.add_column("Database Column", justify="left", style="magenta")
                field_table.add_column("Database Type", justify="left", style="magenta")
                field_table.add_column("Related Model", justify="right", style="dark_red")
                field_table.add_column("Related Name", justify="right", style="dark_red")

            field_table = _fill_table(field_table, info_object_list, info_type, column_count)
            _print_table(field_table)

        def render_field_reverse_relations_table(info_object_list: list or None, info_type: type):
            """Provided a list of FieldReverseRelation objects, prints the resulting sorted table to console"""
            field_table = Table(title="Reverse Relations")
            column_count = 1

            field_table.add_column("Related Name", justify="left", style="yellow", no_wrap=True)
            if VERBOSITY >= 2:
                column_count = 7
                field_table.add_column("Field Type", justify="left", style="magenta")
                field_table.add_column("Database Type", justify="left", style="magenta")
                field_table.add_column("Related Model", justify="right", style="dark_red")
                field_table.add_column("Field Name on Related Model", justify="left", style="dark_red")
                field_table.add_column("Field Type on Related Model", justify="left", style="dark_red")

            field_table = _fill_table(field_table, info_object_list, info_type, column_count)
            _print_table(field_table)

        def render_field_others_table(info_object_list: list or None, info_type: type):
            """Provided a list of FieldOther objects, prints the resulting sorted table to console"""
            field_table = Table(title="Other Fields")
            column_count = 1

            field_table.add_column("Field Name", justify="left", style="yellow", no_wrap=True)
            if VERBOSITY >= 2:
                column_count = 6
                field_table.add_column("Field Type", justify="left", style="magenta")
                field_table.add_column("Database Column", justify="left", style="magenta")
                field_table.add_column("Database Type", justify="left", style="magenta")
                field_table.add_column("Verbose Name", justify="left", style="white")

            field_table = _fill_table(field_table, info_object_list, info_type, column_count)
            _print_table(field_table)

        def render_method_table(info_object_list: list or None, info_type: str):
            """Provided a list of Method objects, prints the resulting sorted table to console"""
            method_table = Table(title=info_type)
            column_count = 1

            method_table.add_column("Method Name", justify="left", style="cyan", no_wrap=True)
            if VERBOSITY > 1:
                column_count = 2
                method_table.add_column("Signature", justify="left", style="magenta")
            if VERBOSITY > 2:
                column_count = 5
                method_table.add_column("Docstring", justify="left", style="magenta")
                method_table.add_column("File", justify="left", style="magenta")
                method_table.add_column("Line Number", justify="left", style="magenta")

            method_table = _fill_table(method_table, info_object_list, Method, column_count)
            _print_table(method_table)

        if MODEL is not None:
            model_list = [django_apps.get_model(MODEL)]
        else:
            model_list = sorted(
                django_apps.get_models(), key=lambda x: (x._meta.app_label, x._meta.object_name), reverse=False
            )
        for model in model_list:
            if VERBOSITY > 0:
                console.print(Padding("", (1, 0, 0, 0)))
                console.print(Padding("", (0, 0, 0, 0), style=section_style))
                console.print(Padding("", (0, 0, 0, 0)))
            console.print(f"{model._meta.label}", style=section_style)

            if VERBOSITY > 0:

                def process_model():
                    build_model_objects(model)
                    model_info = build_model_objects(model)
                    render_model_table(model_info, list)

                process_model()

                def process_fields():
                    console.print(Padding("Fields:", (1, 0, 0, 4), style=subsection_style))

                    field_list = model._meta.get_fields(include_hidden=True)

                    fields_relation, fields_reverse_relation, fields_other = build_field_objects(field_list)

                    render_field_relations_table(fields_relation, FieldRelation)
                    render_field_reverse_relations_table(fields_reverse_relation, FieldReverseRelation)
                    render_field_others_table(fields_other, FieldOther)

                process_fields()

                def get_clean_method_list():
                    """
                    Remove any potential method names that start with an uppercase character, are blank, or not callable
                    """
                    return [
                        method_name
                        for method_name in dir(model)
                        if method_name is not None
                        and not method_name == ""
                        and not method_name[0].isupper()
                        and hasattr(model, method_name)
                        and callable(getattr(model, method_name))
                    ]

                method_list = get_clean_method_list()

                def process_methods():
                    if VERBOSITY == 3:
                        console.print(Padding("Methods (all):", (1, 0, 0, 4), style=subsection_style))
                    else:
                        console.print(Padding("Methods (non-private/internal):", (1, 0, 0, 4), style=subsection_style))

                    method_dunder, method_common_django, method_other_private, method_other = build_method_objects(
                        method_list, model
                    )

                    if VERBOSITY > 1:
                        render_method_table(method_dunder, "Dunder Methods")
                        render_method_table(method_common_django, "Common Django Methods")
                    render_method_table(method_other_private, "Other Private methods")
                    render_method_table(method_other, "Other Methods")

                process_methods()

                self.stdout.write("\n")

        console.print(f"\nTotal Models Listed: {len(model_list)}\n", style=section_style)
        console.print(Align(Bar(size=0.1, begin=0.0, end=0.0, width=100), align="center"), style="red")

        def process_export():
            """If a FILENAME was provided in options, try to save the appropriate type of file"""
            if FILENAME is not None:
                extension = Path(FILENAME).suffixes

                if len(extension) > 0:
                    if any(x in extension[-1] for x in ["htm", "html"]):
                        console.save_html(path=FILENAME)
                        # Using print() to avoid exporting following line
                        print(f"Saved as {FILENAME}")
                    elif "txt" in extension[-1]:
                        console.save_text(path=FILENAME)
                        # Using print() to avoid exporting following line
                        print(f"Saved as {FILENAME}")

        process_export()

    def handle(self, *args, **options):
        self.model_info(options)
