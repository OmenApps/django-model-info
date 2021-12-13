import inspect

from django.db.models import Model


def get_model_name(model: Model) -> str:
    if hasattr(model, "__name__"):
        return str(model.__name__)

    return ""


def get_model_verbose_name(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "verbose_name"):
        return str(model._meta.verbose_name)

    return ""


def get_model_database_table(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "db_table"):
        return str(model._meta.db_table)

    return ""


def get_model_is_abstract(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "abstract"):
        return str(model._meta.abstract)

    return ""


def get_model_is_managed(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "managed"):
        return str(model._meta.managed)

    return ""


def get_model_is_proxy(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "proxy"):
        return str(model._meta.proxy)

    return ""


def get_model_base_manager(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "base_manager_name"):
        return str(model._meta.base_manager_name)

    return ""


def get_model_default_manager(model: Model) -> str:
    if hasattr(model, "_meta") and hasattr(model._meta, "default_manager_name"):
        return str(model._meta.default_manager_name)

    return ""


def get_model_docstring(model: Model) -> str:
    try:
        return str(inspect.getdoc(model))
    except:
        pass

    return ""


def get_model_file(model: Model) -> str:
    try:
        return str(inspect.getfile(model))
    except:
        pass

    return ""


def get_model_line_number(model: Model) -> str:
    try:
        file_info = inspect.getsourcelines(model)
        if len(file_info) > 0:
            return str(file_info[-1])
    except:
        pass

    return ""
