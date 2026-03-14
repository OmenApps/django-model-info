"""Tests for modelinfo_utils/_manager_utils.py."""

from django.db import models

from django_model_info.management.commands.modelinfo_utils._manager_utils import (
    analyze_manager,
    analyze_queryset,
    format_manager_output,
    group_managers_by_name,
    merge_method_info,
)


class TestAnalyzeManager:
    """Tests for analyze_manager."""

    def test_default_manager_returns_none(self):
        assert analyze_manager(models.Manager) is None

    def test_custom_manager_instance(self):
        from example_project.inventory.models import Product

        result = analyze_manager(Product.objects)
        assert result is not None
        assert result["is_custom"] is True
        assert isinstance(result["methods"], dict)


class TestAnalyzeQueryset:
    """Tests for analyze_queryset."""

    def test_default_queryset_returns_none(self):
        assert analyze_queryset(models.QuerySet) is None

    def test_custom_queryset(self):
        from example_project.inventory.models import ProductQuerySet

        result = analyze_queryset(ProductQuerySet)
        assert result is not None
        assert result["name"] == "ProductQuerySet"
        assert "active" in result["methods"]
        assert "low_stock" in result["methods"]
        assert "out_of_stock" in result["methods"]


class TestMergeAndGroupManagerInfo:
    """Tests for merge_method_info, group_managers_by_name, and format_manager_output."""

    def test_merge_method_info_keeps_first(self):
        methods1 = {"foo": {"sig": "(self)"}, "bar": {"sig": "(self, x)"}}
        methods2 = {"foo": {"sig": "(self, override)"}, "baz": {"sig": "(self)"}}
        merged = merge_method_info(methods1, methods2)
        # First occurrence kept for 'foo'
        assert merged["foo"]["sig"] == "(self)"
        assert "bar" in merged
        assert "baz" in merged

    def test_group_managers_by_name(self):
        managers = {
            "objects": {
                "name": "MyManager",
                "module": "app.models",
                "docstring": "doc1",
                "methods": {"method_a": {"sig": "()"}},
            },
            "active_objects": {
                "name": "MyManager",
                "module": "app.models",
                "docstring": "doc2",
                "methods": {"method_b": {"sig": "(x)"}},
            },
        }
        grouped = group_managers_by_name(managers)
        assert "MyManager" in grouped
        # Both manager names should be listed
        assert "objects" in grouped["MyManager"]["manager_names"]
        assert "active_objects" in grouped["MyManager"]["manager_names"]
        # Methods should be merged
        assert "method_a" in grouped["MyManager"]["methods"]
        assert "method_b" in grouped["MyManager"]["methods"]

    def test_format_manager_output_verbosity_zero(self):
        managers = {
            "objects": {
                "name": "MyManager",
                "module": "m",
                "docstring": "",
                "methods": {},
            },
        }
        assert format_manager_output(managers, verbosity=0) == ""

    def test_format_manager_output_verbosity_one(self):
        managers = {
            "objects": {
                "name": "MyManager",
                "module": "m",
                "docstring": "",
                "methods": {},
            },
        }
        result = format_manager_output(managers, verbosity=1)
        assert "Custom Managers:" in result
