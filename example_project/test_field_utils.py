"""Tests for modelfilters_utils/_field_utils.py — pure utility functions."""

import pytest
from django.db import models

from django_model_info.management.commands.modelfilters_utils._field_utils import (
    camel_to_snake,
    matches_target_field_type,
    matches_target_filters,
    normalize_app_model,
    normalize_exclude_pattern,
    normalize_field_path,
    should_skip_field,
)


class TestCamelToSnake:
    """Tests for camel_to_snake conversion."""

    @pytest.mark.parametrize(
        "input_name,expected",
        [
            ("UserProfile", "user_profile"),
            ("HTMLParser", "html_parser"),
            ("simple", "simple"),
            ("A", "a"),
            ("IOError", "io_error"),
            ("getHTTPResponse", "get_http_response"),
        ],
    )
    def test_camel_to_snake_conversion(self, input_name, expected):
        assert camel_to_snake(input_name) == expected


class TestNormalizeExcludePattern:
    """Tests for normalize_exclude_pattern."""

    def test_with_dot_app_model(self):
        assert normalize_exclude_pattern("app.ModelName") == "model_name"

    def test_without_dot(self):
        assert normalize_exclude_pattern("ModelName") == "model_name"

    def test_already_snake_case(self):
        assert normalize_exclude_pattern("model_name") == "model_name"


class TestNormalizeFieldPathAndAppModel:
    """Tests for normalize_field_path and normalize_app_model."""

    def test_normalize_field_path(self):
        assert normalize_field_path("user__Profile") == "user__profile"

    def test_normalize_field_path_multiple_parts(self):
        assert normalize_field_path("customer__User__LogEntry") == "customer__user__log_entry"

    def test_normalize_app_model_with_app(self):
        assert normalize_app_model("auth.Permission") == ("auth", "permission")

    def test_normalize_app_model_without_app(self):
        assert normalize_app_model("Permission") == (None, "permission")


class TestShouldSkipField:
    """Tests for should_skip_field exclusion logic."""

    def test_empty_excludes_returns_false(self):
        assert should_skip_field("some_field", "SomeModel", "app.SomeModel", []) is False

    def test_skip_by_field_path(self):
        """Case 1: exclude pattern with __ matches field path."""
        assert (
            should_skip_field(
                "customer__user__logentry",
                "LogEntry",
                "common.Customer,auth.User",
                ["customer__user"],
            )
            is True
        )

    def test_skip_by_app_model(self):
        """Case 2: exclude with dot matches app.Model in path."""
        assert (
            should_skip_field(
                "some_field",
                "Permission",
                "auth.Permission",
                ["auth.Permission"],
            )
            is True
        )

    def test_skip_by_model_name(self):
        """Case 3: plain model name matches current model."""
        assert (
            should_skip_field(
                "perm",
                "Permission",
                "auth.Permission",
                ["Permission"],
            )
            is True
        )

    def test_no_match_returns_false(self):
        assert (
            should_skip_field(
                "some_field",
                "Product",
                "inventory.Product",
                ["Category"],
            )
            is False
        )


class TestMatchesTargetFilters:
    """Tests for matches_target_field_type and matches_target_filters."""

    def test_target_field_type_none_always_true(self):
        """None target means no filter — always matches."""
        field = models.CharField()
        assert matches_target_field_type(field, None) is True

    def test_target_field_type_matching(self):
        field = models.CharField()
        assert matches_target_field_type(field, "CharField") is True

    def test_target_field_type_not_matching(self):
        field = models.CharField()
        assert matches_target_field_type(field, "IntegerField") is False

    def test_matches_target_filters_no_filters(self):
        """No target_model and no target_field means everything matches."""
        from example_project.inventory.models import Product

        assert matches_target_filters(Product, "name", None, None) is True

    def test_matches_target_filters_with_target_model_match(self):
        from example_project.inventory.models import Category, Product

        assert matches_target_filters(Product, "name", Product, None) is True
        assert matches_target_filters(Product, "name", Category, None) is False

    def test_matches_target_filters_with_target_field_string(self):
        from example_project.inventory.models import Product

        assert matches_target_filters(Product, "name", None, "name") is True
        assert matches_target_filters(Product, "name", None, "sku") is False

    def test_matches_target_filters_with_target_field_list(self):
        from example_project.inventory.models import Product

        assert matches_target_filters(Product, "name", None, ["name", "sku"]) is True
        assert matches_target_filters(Product, "name", None, ["sku", "price"]) is False
