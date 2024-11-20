"""Get model attributes."""

import inspect

from django.db.models import Model


def get_model_name(model: Model) -> str:
    """Get the name of the model."""
    if hasattr(model, "__name__"):
        return str(model.__name__)

    return ""


def get_model_verbose_name(model: Model) -> str:
    """Get the verbose name of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "verbose_name"):  # pylint: disable=W0212
        return str(model._meta.verbose_name)  # pylint: disable=W0212

    return ""


def get_model_verbose_name_plural(model: Model) -> str:
    """Get the verbose name plural of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "verbose_name_plural"):  # pylint: disable=W0212
        return str(model._meta.verbose_name_plural)  # pylint: disable=W0212

    return ""


def get_model_database_table(model: Model) -> str:
    """Get the database table of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "db_table"):  # pylint: disable=W0212
        return str(model._meta.db_table)  # pylint: disable=W0212

    return ""


def get_model_database_table_comment(model: Model) -> str:
    """Get the database table comment of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "db_table_comment"):  # pylint: disable=W0212
        return str(model._meta.db_table_comment)  # pylint: disable=W0212

    return ""


def get_model_database_tablespace(model: Model) -> str:
    """Get the database tablespace of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "db_tablespace"):  # pylint: disable=W0212
        return str(model._meta.db_tablespace)  # pylint: disable=W0212

    return ""


def get_model_is_abstract(model: Model) -> str:
    """Get the abstract status of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "abstract"):  # pylint: disable=W0212
        return str(model._meta.abstract)  # pylint: disable=W0212

    return ""


def get_model_is_managed(model: Model) -> str:
    """Get the managed status of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "managed"):  # pylint: disable=W0212
        return str(model._meta.managed)  # pylint: disable=W0212

    return ""


def get_model_is_proxy(model: Model) -> str:
    """Get the proxy model status of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "proxy"):  # pylint: disable=W0212
        return str(model._meta.proxy)  # pylint: disable=W0212

    return ""


def get_model_base_manager(model: Model) -> str:
    """Get the base manager of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "base_manager_name"):  # pylint: disable=W0212
        return str(model._meta.base_manager_name)  # pylint: disable=W0212

    return ""


def get_model_default_manager(model: Model) -> str:
    """Get the default manager of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "default_manager_name"):  # pylint: disable=W0212
        return str(model._meta.default_manager_name)  # pylint: disable=W0212

    return ""


def get_model_ordering(model: Model) -> str:
    """Get the ordering of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "ordering"):  # pylint: disable=W0212
        return str(model._meta.ordering)  # pylint: disable=W0212

    return ""


def get_model_permissions(model: Model) -> str:
    """Get the permissions of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "permissions"):  # pylint: disable=W0212
        return str(model._meta.permissions)  # pylint: disable=W0212

    return ""


def get_model_default_permissions(model: Model) -> str:
    """Get the default_permissions of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "default_permissions"):  # pylint: disable=W0212
        return str(model._meta.default_permissions)  # pylint: disable=W0212

    return ""


def get_model_indexes(model: Model) -> str:
    """Get the indexes of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "indexes"):  # pylint: disable=W0212
        return str(model._meta.indexes)  # pylint: disable=W0212

    return ""


def get_model_constraints(model: Model) -> str:
    """Get the constraints of the model."""
    if hasattr(model, "_meta") and hasattr(model._meta, "constraints"):  # pylint: disable=W0212
        return str(model._meta.constraints)  # pylint: disable=W0212

    return ""


def get_model_docstring(model: Model) -> str:
    """Get the docstring of the model."""
    try:
        return str(inspect.getdoc(model))
    except AttributeError:
        pass
    except OSError:
        pass

    return ""


def get_model_file(model: Model) -> str:
    """Get the file where the model is defined."""
    try:
        return str(inspect.getfile(model))
    except AttributeError:
        pass
    except OSError:
        pass

    return ""


def get_model_line_number(model: Model) -> str:
    """Get the line number where the model is defined."""
    try:
        file_info = inspect.getsourcelines(model)
        if len(file_info) > 0:
            return str(file_info[-1])
    except AttributeError:
        pass
    except OSError:
        pass

    return ""


def get_model_mro(model: Model) -> str:
    """Get the method resolution order of the model."""
    try:
        return str(inspect.getmro(model))
    except AttributeError:
        pass
    except OSError:
        pass

    return
