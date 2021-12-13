import inspect


def get_method_signature(method: str, model: type, verbosity: int) -> str:
    if verbosity > 1:

        try:
            return str(inspect.signature(getattr(model, method)))
        except ValueError:
            return "ValueError no signature found"
        except TypeError as e:
            return f"TypeError {e}"
        except Exception as e:
            return f"{e}"

    return ""


def get_method_docstring(method: str, model: type) -> str:
    try:
        return inspect.getdoc(getattr(model, method))
    except:
        pass

    return ""


def get_method_file(method: str, model: type) -> str:
    try:
        return inspect.getfile(getattr(model, method))
    except:
        pass

    return ""


def get_method_line_number(method: str, model: type) -> str:
    try:
        file_info = inspect.getsourcelines(getattr(model, method))
        if len(file_info) > 0:
            return str(file_info[-1])
    except:
        pass

    return ""
