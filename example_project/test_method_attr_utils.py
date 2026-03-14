"""Tests for modelinfo_utils/_method_attr_utils.py."""

from django_model_info.management.commands.modelinfo_utils._method_attr_utils import (
    get_method_docstring,
    get_method_file,
    get_method_line_number,
    get_method_signature,
    shorten_path,
)


class TestShortenPath:
    """Tests for shorten_path."""

    def test_shorten_path_length_3(self):
        result = str(shorten_path("/home/user/project/src/models.py", 3))
        assert result.endswith("src/models.py") or result.endswith("src\\models.py")
        assert "project" in result

    def test_shorten_path_length_1(self):
        result = str(shorten_path("/home/user/project/src/models.py", 1))
        assert result == "models.py"


class TestGetMethodSignature:
    """Tests for get_method_signature with verbosity levels and error paths."""

    def test_verbosity_zero_returns_empty(self):
        from example_project.inventory.models import Product

        assert get_method_signature("clean", Product, verbosity=0) == ""

    def test_verbosity_one_returns_empty(self):
        from example_project.inventory.models import Product

        assert get_method_signature("clean", Product, verbosity=1) == ""

    def test_verbosity_two_returns_signature(self):
        from example_project.inventory.models import Product

        result = get_method_signature("clean", Product, verbosity=2)
        assert result != ""
        assert "self" in result

    def test_value_error_returns_no_signature_found(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_value_error(*a, **kw):
            raise ValueError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "signature", raise_value_error)
        result = get_method_signature("clean", Product, verbosity=2)
        assert result == "No signature found"

    def test_type_error_returns_empty(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_type_error(*a, **kw):
            raise TypeError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "signature", raise_type_error)
        result = get_method_signature("clean", Product, verbosity=2)
        assert result == ""


class TestGetMethodDocstring:
    """Tests for get_method_docstring."""

    def test_happy_path(self):
        from example_project.inventory.models import Product

        result = get_method_docstring("clean", Product)
        # clean doesn't have a docstring in the model, but getdoc may return None
        # Just verify it doesn't raise
        assert result is None or isinstance(result, str)

    def test_attribute_error_returns_error_string(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_attr_error(*a, **kw):
            raise AttributeError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "getdoc", raise_attr_error)
        result = get_method_docstring("clean", Product)
        assert "AttributeError" in result

    def test_os_error_returns_empty(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_os_error(*a, **kw):
            raise OSError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "getdoc", raise_os_error)
        result = get_method_docstring("clean", Product)
        assert result == ""


class TestGetMethodFileAndLineNumber:
    """Tests for get_method_file and get_method_line_number."""

    def test_get_method_file_happy_path(self):
        from example_project.inventory.models import Product

        result = get_method_file("clean", Product)
        assert "models" in result

    def test_get_method_line_number_happy_path(self):
        from example_project.inventory.models import Product

        result = get_method_line_number("clean", Product)
        assert result.isdigit()

    def test_get_method_file_type_error_returns_empty(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_type_error(*a, **kw):
            raise TypeError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "getfile", raise_type_error)
        result = get_method_file("clean", Product)
        assert result == ""

    def test_get_method_line_number_type_error_returns_empty(self, monkeypatch):
        from django_model_info.management.commands.modelinfo_utils import _method_attr_utils

        from example_project.inventory.models import Product

        def raise_type_error(*a, **kw):
            raise TypeError("test")

        monkeypatch.setattr(_method_attr_utils.inspect, "getsourcelines", raise_type_error)
        result = get_method_line_number("clean", Product)
        assert result == ""
