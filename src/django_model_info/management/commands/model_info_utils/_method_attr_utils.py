"""Get method attributes for a model."""

import inspect
from pathlib import Path

from rich.errors import NotRenderableError


def shorten_path(file_path, length):
    """Split the path into separate parts, select the last
    ...     'length' elements and join them again"""
    return Path(*Path(file_path).parts[-length:])


def get_method_signature(method: str, model: type, verbosity: int) -> str:
    """Get the method signature."""
    if verbosity > 1:

        try:
            return str(inspect.signature(getattr(model, method)))
        except ValueError:
            return "No signature found"
        except TypeError:
            pass
        except OSError:
            pass
        except Exception:  # pylint: disable=W0718
            pass

    return ""


def get_method_docstring(method: str, model: type) -> str:
    """Get the method docstring."""
    try:
        return inspect.getdoc(getattr(model, method))
    except AttributeError as e:
        return f"AttributeError {e}"
    except OSError:
        pass

    return ""


def get_method_file(method: str, model: type) -> str:
    """Get the file where the method is defined."""
    try:
        file = inspect.getfile(getattr(model, method))
        return str(shorten_path(file, 6))
    except AttributeError:
        pass
    except TypeError:
        pass
    except NotRenderableError:
        pass
    except OSError:
        pass

    return ""


def get_method_line_number(method: str, model: type) -> str:
    """Get the line number where the method is defined."""
    try:
        file_info = inspect.getsourcelines(getattr(model, method))
        if len(file_info) > 0:
            return str(file_info[-1])
    except AttributeError:
        pass
    except TypeError:
        pass
    except OSError:
        pass

    return ""
