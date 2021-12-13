from django.db import connection
from django.db.models import Field


def get_field_name(field: Field) -> str:
    if hasattr(field, "name"):
        field_name = field.name
        if hasattr(field, "primary_key") and field.primary_key:
            field_name = f"{field_name} (pk)"
        return field_name

    return ""


def get_field_column(field: Field) -> str:
    if hasattr(field, "column"):
        return str(field.column)

    return ""


def get_field_verbose_name(field: Field) -> str:
    if hasattr(field, "verbose_name"):
        return str(field.verbose_name)

    return ""


def get_field_db_type(field: Field) -> str:
    db_type = "None"
    if hasattr(field, "db_type"):
        try:
            db_type = str(field.db_type(connection=connection))
        except TypeError:
            db_type = " TypeError (db_type)"
        except AttributeError:
            db_type = " AttributeError (db_type)"

        if db_type == "None" and hasattr(field, "through"):
            db_type = f"through {field.through._meta.label}"

        if db_type == "None" and (
            hasattr(field, "remote_field") and field.remote_field is not None and hasattr(field.remote_field, "through")
        ):
            db_type = f"through {field.remote_field.through._meta.label}"
        return db_type

    return db_type


def get_related_name(field: Field) -> str:
    if hasattr(field, "related_name") and field.related_name is not None:
        field_related_name = str(field.related_name)
        if "+" in field_related_name:
            return f"{field_related_name} (no reverse relation allowed)"
        return field_related_name

    elif (
        hasattr(field, "remote_field")
        and field.remote_field is not None
        and hasattr(field.remote_field, "related_name")
    ):
        return str(field.remote_field.related_name)

    return "(None)"


def get_field_name_on_reverse_model(field: Field) -> str:
    if hasattr(field, "field") and field.field is not None:
        return str(field.field.name)

    return ""


def get_field_type_on_reverse_model(field: Field) -> str:
    if hasattr(field, "field"):
        return str(field.field.get_internal_type())

    return ""


def get_field_type(field: Field) -> str:
    if hasattr(field, "__class__"):
        return str(field.__class__.__name__)
    elif hasattr(field, "get_internal_type"):
        return str(field.get_internal_type())

    return ""


def get_related_model(field: Field) -> str:
    if hasattr(field, "related_model") and field.related_model is not None:
        return str(field.related_model._meta.label)

    return ""
