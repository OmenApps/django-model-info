"""Tests for modelinfo_utils/_model_attr_utils.py."""

from django_model_info.management.commands.modelinfo_utils._model_attr_utils import (
    get_model_database_table,
    get_model_docstring,
    get_model_file,
    get_model_is_abstract,
    get_model_is_managed,
    get_model_is_proxy,
    get_model_line_number,
    get_model_mro,
    get_model_name,
    get_model_ordering,
    get_model_verbose_name,
)


class TestModelAttrGettersWithRealModel:
    """Test all getters with a real Django model."""

    def test_model_attr_getters_with_product(self):
        from example_project.inventory.models import Product

        assert get_model_name(Product) == "Product"
        assert get_model_verbose_name(Product) != ""
        assert "product" in get_model_database_table(Product).lower()
        assert get_model_is_abstract(Product) == "False"
        assert get_model_ordering(Product) == "[]"
        assert get_model_docstring(Product) != ""
        assert "models.py" in get_model_file(Product)
        # Line number should be a numeric string
        line_num = get_model_line_number(Product)
        assert line_num.isdigit()


class TestModelAttrGettersAbstractAndProxy:
    """Test abstract, proxy, and unmanaged model detection."""

    def test_abstract_model(self):
        from example_project.common.models import BaseModel

        assert get_model_is_abstract(BaseModel) == "True"

    def test_proxy_model(self):
        from example_project.analytics.models import CustomerSegment

        assert get_model_is_proxy(CustomerSegment) == "True"

    def test_unmanaged_model(self):
        from example_project.analytics.models import DailyRevenue

        assert get_model_is_managed(DailyRevenue) == "False"


class TestModelAttrErrorBranches:
    """Test exception handling branches in getters."""

    def test_get_model_docstring_attribute_error(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _model_attr_utils

        from example_project.inventory.models import Product

        def raise_attr_error(*a, **kw):
            raise AttributeError("test")

        monkeypatch.setattr(_model_attr_utils.inspect, "getdoc", raise_attr_error)
        assert get_model_docstring(Product) == ""

    def test_get_model_file_os_error(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _model_attr_utils

        from example_project.inventory.models import Product

        def raise_os_error(*a, **kw):
            raise OSError("test")

        monkeypatch.setattr(_model_attr_utils.inspect, "getfile", raise_os_error)
        assert get_model_file(Product) == ""

    def test_get_model_line_number_os_error(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _model_attr_utils

        from example_project.inventory.models import Product

        def raise_os_error(*a, **kw):
            raise OSError("test")

        monkeypatch.setattr(_model_attr_utils.inspect, "getsourcelines", raise_os_error)
        assert get_model_line_number(Product) == ""


class TestGetModelMro:
    """Test get_model_mro."""

    def test_mro_contains_model_names(self):
        from example_project.inventory.models import Product

        result = get_model_mro(Product)
        assert "Product" in result
        assert "Model" in result

    def test_mro_returns_none_not_empty_string(self, monkeypatch):
        """Line 183 returns None (implicit) — document the inconsistency."""
        from django_model_info.management.commands.modelinfo_utils import _model_attr_utils

        from example_project.inventory.models import Product

        def raise_attr_error(*a, **kw):
            raise AttributeError("test")

        monkeypatch.setattr(_model_attr_utils.inspect, "getmro", raise_attr_error)
        result = get_model_mro(Product)
        # The function returns None (implicit return) on error, not ""
        assert result is None
