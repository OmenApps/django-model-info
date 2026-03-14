"""Tests for the modelgraph management command."""

import shutil

import pytest
from django.core.management import call_command


class TestModelGraphCommand:
    """Tests for the modelgraph management command."""

    def test_analysis_format_default(self, capsys):
        """Default format (analysis) produces output."""
        call_command("modelgraph")
        output = capsys.readouterr().out
        assert output, "modelgraph analysis should produce output"

    def test_analysis_format_explicit(self, capsys):
        """Explicit analysis format works."""
        call_command("modelgraph", "-f", "analysis")
        output = capsys.readouterr().out
        assert output

    def test_mermaid_format(self, capsys):
        """Mermaid format produces mermaid syntax."""
        call_command("modelgraph", "-f", "mermaid")
        output = capsys.readouterr().out
        assert output
        assert "graph" in output.lower() or "---" in output or "-->" in output

    @pytest.mark.skipif(shutil.which("dot") is None, reason="graphviz 'dot' binary not installed")
    def test_dot_format(self, tmp_path):
        """DOT format writes a valid dot file."""
        path = tmp_path / "output.dot"
        call_command("modelgraph", "-f", "dot", "-o", str(path))
        content = path.read_text()
        assert "digraph" in content or "graph" in content.lower()

    def test_filter_by_app(self, capsys):
        """Command filters by app label."""
        call_command("modelgraph", "inventory", "-f", "analysis")
        output = capsys.readouterr().out
        assert output

    def test_exclude_app(self, capsys):
        """Command excludes specified apps."""
        call_command("modelgraph", "-e", "analytics", "-f", "analysis")

    def test_include_abstract(self, capsys):
        """Command includes abstract models with -a."""
        call_command("modelgraph", "-a", "-f", "analysis")

    def test_include_proxy(self, capsys):
        """Command includes proxy models with -p."""
        call_command("modelgraph", "-p", "-f", "analysis")
