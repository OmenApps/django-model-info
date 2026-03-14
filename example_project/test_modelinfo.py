"""Tests for the modelinfo management command."""

from django.core.management import call_command


class TestModelInfoCommand:
    """Tests for the modelinfo management command."""

    def test_runs_without_args(self, capsys):
        """Command runs successfully with no arguments."""
        call_command("modelinfo")
        output = capsys.readouterr().out
        assert output, "modelinfo should produce output"

    def test_filter_by_app(self, capsys):
        """Command filters by app label."""
        call_command("modelinfo", "inventory")
        output = capsys.readouterr().out
        assert "inventory" in output.lower()

    def test_filter_by_model(self, capsys):
        """Command filters by app.Model."""
        call_command("modelinfo", "inventory.Product")
        output = capsys.readouterr().out
        assert "Product" in output

    def test_exclude_defaults(self, capsys):
        """Command runs with --exclude-defaults."""
        call_command("modelinfo", "--exclude-defaults", "inventory.Product")
        output = capsys.readouterr().out
        assert "Product" in output

    def test_verbosity_zero(self, capsys):
        """Command runs at verbosity 0 (model names only)."""
        call_command("modelinfo", verbosity=0)

    def test_verbosity_one(self, capsys):
        """Command runs at verbosity 1."""
        call_command("modelinfo", "inventory.Product", verbosity=1)

    def test_verbosity_three(self, capsys):
        """Command runs at verbosity 3 (max detail)."""
        call_command("modelinfo", "inventory.Product", verbosity=3)

    def test_markdown_output(self, capsys):
        """Command produces markdown when --markdown is passed."""
        call_command("modelinfo", "--markdown", "inventory.Product")
        output = capsys.readouterr().out
        assert "#" in output or "Product" in output

    def test_export_to_txt(self, capsys, tmp_path):
        """Command exports to a .txt file."""
        path = tmp_path / "output.txt"
        call_command("modelinfo", "-o", str(path), "inventory.Product")
        assert path.read_text(), "Exported txt file should not be empty"

    def test_export_to_md(self, capsys, tmp_path):
        """Command exports to a .md file."""
        path = tmp_path / "output.md"
        call_command("modelinfo", "-o", str(path), "inventory.Product")
        assert path.read_text(), "Exported md file should not be empty"

    def test_export_to_html(self, capsys, tmp_path):
        """Command exports to an .html file."""
        path = tmp_path / "output.html"
        call_command("modelinfo", "-o", str(path), "inventory.Product")
        content = path.read_text()
        assert "html" in content.lower() or "Product" in content
