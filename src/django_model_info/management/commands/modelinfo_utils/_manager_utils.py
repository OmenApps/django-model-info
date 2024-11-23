"""Utility functions for analyzing model managers and querysets."""
import inspect

from django.db import models
from django.db.models.manager import Manager
from django.db.models.query import QuerySet


def analyze_manager(manager_class):
    """Analyze a model Manager class.

    Args:
        manager_class: Django Manager class

    Returns:
        dict: Manager analysis information
    """
    # Skip if this is the default manager
    if manager_class == models.Manager:
        return None

    # Get the actual class (not instance)
    if isinstance(manager_class, Manager):
        manager_class = manager_class.__class__

    info = {
        "name": manager_class.__name__,
        "docstring": inspect.getdoc(manager_class),
        "methods": {},
        "is_custom": manager_class != models.Manager,
        "module": manager_class.__module__,
    }

    # Get custom methods (skip those from base Manager)
    base_methods = set(dir(models.Manager))
    for name, method in inspect.getmembers(manager_class, predicate=inspect.isfunction):
        if name not in base_methods and not name.startswith("_"):
            info["methods"][name] = {
                "docstring": inspect.getdoc(method),
                "signature": str(inspect.signature(method)),
                "source_file": inspect.getsourcefile(method),
                "line_number": inspect.getsourcelines(method)[1],
            }

    return info


def analyze_queryset(queryset_class):
    """Analyze a model QuerySet class.

    Args:
        queryset_class: Django QuerySet class

    Returns:
        dict: QuerySet analysis information
    """
    # Skip if this is the default queryset
    if queryset_class == models.QuerySet:
        return None

    # Get the actual class (not instance)
    if isinstance(queryset_class, QuerySet):
        queryset_class = queryset_class.__class__

    info = {
        "name": queryset_class.__name__,
        "docstring": inspect.getdoc(queryset_class),
        "methods": {},
        "is_custom": queryset_class != models.QuerySet,
        "module": queryset_class.__module__,
    }

    # Get custom methods (skip those from base QuerySet)
    base_methods = set(dir(models.QuerySet))
    for name, method in inspect.getmembers(queryset_class, predicate=inspect.isfunction):
        if name not in base_methods and not name.startswith("_"):
            info["methods"][name] = {
                "docstring": inspect.getdoc(method),
                "signature": str(inspect.signature(method)),
                "source_file": inspect.getsourcefile(method),
                "line_number": inspect.getsourcelines(method)[1],
            }

    return info


def get_model_managers(model):
    """Get all managers for a model, including custom managers.

    Args:
        model: Django model class

    Returns:
        dict: Manager information
    """
    managers = {}

    # Get default manager
    if hasattr(model._meta, "default_manager"):
        default_manager = model._meta.default_manager
        if default_manager.__class__ != models.Manager:
            managers["default"] = analyze_manager(default_manager)
            queryset_class = default_manager._queryset_class
            if queryset_class != models.QuerySet:
                managers["default"]["queryset"] = analyze_queryset(queryset_class)

    # Get additional managers from _meta
    if hasattr(model._meta, "_managers"):
        for manager in model._meta._managers:
            if isinstance(manager, Manager) and manager.__class__ != models.Manager:
                name = manager.name if hasattr(manager, "name") else "unnamed"
                manager_info = analyze_manager(manager)
                if manager_info:
                    managers[name] = manager_info
                    queryset_class = manager._queryset_class
                    if queryset_class != models.QuerySet:
                        managers[name]["queryset"] = analyze_queryset(queryset_class)

    # Check for manager attributes directly on model
    for attr_name in dir(model):
        attr = getattr(model, attr_name)
        if isinstance(attr, Manager) and attr.__class__ != models.Manager:
            manager_info = analyze_manager(attr)
            if manager_info:
                managers[attr_name] = manager_info
                queryset_class = attr._queryset_class
                if queryset_class != models.QuerySet:
                    managers[attr_name]["queryset"] = analyze_queryset(queryset_class)

    return managers if managers else None


def merge_method_info(methods1, methods2):
    """Merge two method dictionaries, combining any duplicate method names.

    In case of duplicates, keeps the first occurrence's information.
    """
    merged = methods1.copy()
    for method_name, method_info in methods2.items():
        if method_name not in merged:
            merged[method_name] = method_info
    return merged


def merge_manager_info(info1, info2):
    """Merge two manager info dictionaries, combining their methods and querysets."""
    merged = {
        "name": info1["name"],
        "module": info1.get("module", ""),
        "docstring": info1.get("docstring", "") or info2.get("docstring", ""),
        "methods": merge_method_info(info1.get("methods", {}), info2.get("methods", {})),
    }

    # Merge querysets if present
    queryset1 = info1.get("queryset")
    queryset2 = info2.get("queryset")
    if queryset1 or queryset2:
        if queryset1 and queryset2 and queryset1["name"] == queryset2["name"]:
            # Combine querysets with the same name
            merged["queryset"] = {
                "name": queryset1["name"],
                "module": queryset1.get("module", ""),
                "docstring": queryset1.get("docstring", "") or queryset2.get("docstring", ""),
                "methods": merge_method_info(queryset1.get("methods", {}), queryset2.get("methods", {})),
            }
        else:
            # Keep the first queryset if they're different
            merged["queryset"] = queryset1 or queryset2

    return merged


def group_managers_by_name(managers_info):
    """Group managers by their class name and merge their information."""
    grouped = {}
    for manager_name, manager_info in managers_info.items():
        class_name = manager_info["name"]
        if class_name in grouped:
            # Merge this manager's info with existing info for this class
            grouped[class_name] = merge_manager_info(grouped[class_name], manager_info)
            # Add this manager name to the list of names
            grouped[class_name]["manager_names"] = grouped[class_name].get("manager_names", []) + [manager_name]
        else:
            # First occurrence of this class name
            grouped[class_name] = manager_info.copy()
            grouped[class_name]["manager_names"] = [manager_name]
    return grouped


def format_manager_output(managers_info, indent=0, verbosity=0):
    """Format manager information for display, combining managers with the same class name.

    Args:
        managers_info: Dict containing manager information
        indent: Number of spaces to indent
        verbosity: Level of detail to include
    Returns:
        str: Formatted output string
    """
    if not managers_info or verbosity < 1:
        return ""

    output = []
    indent_str = " " * indent
    output.append(f"{indent_str}Custom Managers:")

    # Group managers by their class name
    grouped_managers = group_managers_by_name(managers_info)

    # Format output for each unique manager class
    for class_name, manager_info in grouped_managers.items():
        # List all manager names that use this class
        manager_names = manager_info.get("manager_names", [])
        output.append(f"{indent_str}  {', '.join(manager_names)}:")
        output.append(f"{indent_str}    Class: {class_name}")

        if verbosity > 1:
            output.append(f"{indent_str}    Module: {manager_info['module']}")

        if manager_info["docstring"]:
            output.append(f"{indent_str}    Description: {manager_info['docstring']}")

        if manager_info["methods"]:
            output.append(f"{indent_str}    Custom Methods:")
            for method_name, method_info in manager_info["methods"].items():
                output.append(f"{indent_str}      {method_name}{method_info['signature']}")
                if method_info["docstring"]:
                    output.append(f"{indent_str}        {method_info['docstring']}")

        if "queryset" in manager_info:
            output.append(f"{indent_str}Custom QuerySet:")
            queryset_info = manager_info["queryset"]
            output.append(f"{indent_str}    Class: {queryset_info['name']}")

            if verbosity > 2:
                output.append(f"{indent_str}    Module: {queryset_info['module']}")

            if queryset_info["docstring"]:
                output.append(f"{indent_str}    Description: {queryset_info['docstring']}")

            if queryset_info["methods"]:
                output.append(f"{indent_str}    Custom Methods:")
                for method_name, method_info in queryset_info["methods"].items():
                    output.append(f"{indent_str}      {method_name}{method_info['signature']}")
                    if method_info["docstring"]:
                        output.append(f"{indent_str}        {method_info['docstring']}")
                    if verbosity > 2 and method_info["source_file"] and method_info["line_number"]:
                        output.append(f"{indent_str}        {method_info['source_file']}:{method_info['line_number']}")

    return "\n".join(output)
