"""Tests for the migrationgraph management command."""

from io import StringIO

from django.core.management import call_command


class TestMigrationGraphCommand:
    """Tests for the migrationgraph management command."""

    def test_runs_without_args(self):
        """Command runs and produces a mermaid flowchart."""
        out = StringIO()
        call_command("migrationgraph", stdout=out)
        output = out.getvalue()
        assert output, "migrationgraph should produce output"
        assert "flowchart" in output.lower() or "mermaid" in output.lower() or "-->" in output

    def test_filter_by_app_label(self):
        """Command filters by app label."""
        out = StringIO()
        call_command("migrationgraph", "inventory", stdout=out)
        assert out.getvalue()

    def test_multiple_app_labels(self):
        """Command accepts multiple app labels."""
        out = StringIO()
        call_command("migrationgraph", "inventory", "sales", stdout=out)
        assert out.getvalue()
