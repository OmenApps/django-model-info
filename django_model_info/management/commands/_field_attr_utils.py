"""Get field attributes for a model field."""

from django.db import connection
from django.db.models import Field, Model


def get_field_name(field: Field) -> str:
    """Get the name of the field."""
    if hasattr(field, "name"):
        field_name = field.name
        if hasattr(field, "primary_key") and field.primary_key:
            field_name = f"{field_name} (pk)"
        return field_name

    return ""


def get_field_column(field: Field) -> str:
    """Get the column name of the field."""
    if hasattr(field, "column"):
        return str(field.column)

    return ""


def get_field_verbose_name(field: Field) -> str:
    """Get the verbose name of the field."""
    if hasattr(field, "verbose_name"):
        return str(field.verbose_name)

    return ""


def get_field_db_type(field: Field) -> str:
    """Get the database type of the field."""
    db_type = "None"
    if hasattr(field, "db_type"):
        try:
            db_type = str(field.db_type(connection=connection))
        except TypeError:
            db_type = " TypeError (db_type)"
        except AttributeError:
            db_type = " AttributeError (db_type)"

        if db_type == "None" and hasattr(field, "through"):
            db_type = f"through {field.through._meta.label}"  # pylint: disable=W0212

        if db_type == "None" and (
            hasattr(field, "remote_field") and field.remote_field is not None and hasattr(field.remote_field, "through")
        ):
            db_type = f"through {field.remote_field.through._meta.label}"  # pylint: disable=W0212
        return db_type

    return db_type


def get_related_name(field: Field, model: Model) -> str:
    """Get the related name of the field."""
    if hasattr(field, "related_name") and field.related_name is not None:
        field_related_name = str(field.related_name)
        if "+" in field_related_name:
            return f"{field_related_name} (no reverse relation allowed)"
        return field_related_name

    elif (
        hasattr(field, "remote_field")
        and field.remote_field is not None
        and hasattr(field.remote_field, "related_name")
        and field.remote_field.related_name is not None
    ):
        return str(field.remote_field.related_name)

    return f"{model._meta.label_lower.split('.')[-1]}_set"  # pylint: disable=W0212


def get_field_name_on_reverse_model(field: Field) -> str:
    """Get the field name on the related model."""
    if hasattr(field, "field") and field.field is not None:
        return str(field.field.name)

    return ""


def get_field_type_on_reverse_model(field: Field) -> str:
    """Get the field type on the related model."""
    if hasattr(field, "field"):
        return str(field.field.get_internal_type())

    return ""


def get_field_type(field: Field) -> str:
    """Get the type of the field."""
    if hasattr(field, "__class__"):
        return str(field.__class__.__name__)
    elif hasattr(field, "get_internal_type"):
        return str(field.get_internal_type())

    return ""


def get_related_model(field: Field) -> str:
    """Get the related model of the field."""
    if hasattr(field, "related_model") and field.related_model is not None:
        return str(field.related_model._meta.label)  # pylint: disable=W0212

    return ""
