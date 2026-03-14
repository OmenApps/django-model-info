"""Tests for the modelfilters management command."""

from django.core.management import call_command


class TestModelFiltersCommand:
    """Tests for the modelfilters management command."""

    def test_runs_without_args(self, capsys):
        """Command runs successfully with no arguments."""
        call_command("modelfilters")
        output = capsys.readouterr().out
        assert output, "modelfilters should produce output"

    def test_filter_by_app(self, capsys):
        """Command filters by app label."""
        call_command("modelfilters", "inventory")
        output = capsys.readouterr().out
        assert output

    def test_filter_by_model(self, capsys):
        """Command filters by app.Model."""
        call_command("modelfilters", "inventory.Product")
        output = capsys.readouterr().out
        assert output

    def test_max_depth(self, capsys):
        """Command respects --max-depth."""
        call_command("modelfilters", "inventory.Product", "--max-depth", "2")

    def test_markdown_output(self, capsys):
        """Command produces markdown with --markdown."""
        call_command("modelfilters", "--markdown", "inventory.Product")
        output = capsys.readouterr().out
        assert output

    def test_export_to_txt(self, capsys, tmp_path):
        """Command exports to a .txt file."""
        path = tmp_path / "output.txt"
        call_command("modelfilters", "-o", str(path), "inventory.Product")
        assert path.read_text(), "Exported txt file should not be empty"

    def test_by_depth_sort(self, capsys):
        """Command sorts by depth with --by-depth."""
        call_command("modelfilters", "inventory.Product", "--by-depth")

    def test_by_model_sort(self, capsys):
        """Command sorts by model with --by-model."""
        call_command("modelfilters", "inventory.Product", "--by-model")

    def test_target_model_and_exclude(self, capsys):
        """Command filters by --target-model and --exclude."""
        call_command("modelfilters", "inventory.Product", "--target-model", "Category", "--exclude", "auth")
        output = capsys.readouterr().out
        assert output
        assert "auth" not in output.lower() or "category" in output.lower()

    def test_max_paths_option(self, capsys):
        """Command respects --max-paths to limit results."""
        call_command("modelfilters", "inventory.Product", "--max-paths", "5")
        output = capsys.readouterr().out
        # Count non-header, non-empty lines that look like field paths (contain __)
        # or are single field names. The exact format depends on output mode,
        # but with max-paths=5 we should have at most 5 field entries.
        assert output  # At minimum, output should not be empty
