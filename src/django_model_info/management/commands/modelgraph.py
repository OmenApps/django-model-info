"""Django management command for generating model relationship graphs."""
from pathlib import Path
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from .modelgraph_utils._analysis import TextAnalysisOutputFormat
from .modelgraph_utils._dot import DotOutputFormat
from .modelgraph_utils._graph import build_modelgraph, get_model_list
from .modelgraph_utils._mermaidjs import MermaidOutputFormat

try:
    import networkx as nx
    import pydot
except ImportError as e:
    raise ImportError("The networkx and pydot packages are required for this command.") from e


class Command(BaseCommand):
    """Django management command to generate model relationship graphs."""

    help = "Generate a graph showing relationships between models"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.output_path: Optional[Path] = None
        self.output_format: Optional[str] = None

    def add_arguments(self, parser: CommandParser) -> None:
        """Add command arguments."""
        parser.add_argument(
            "filter",
            nargs="*",
            type=str,
            help="Apps, models, or app.Model to graph",
        )
        parser.add_argument(
            "-e",
            "--exclude",
            nargs="+",
            type=str,
            help="Apps, models, or app.Model to exclude",
        )
        parser.add_argument(
            "--prefix",
            type=str,
            help="Include only models with this prefix",
        )
        parser.add_argument(
            "-a",
            "--abstract",
            action="store_true",
            help="Include abstract models in graph",
        )
        parser.add_argument(
            "-p",
            "--proxy",
            action="store_true",
            help="Include proxy models in graph",
        )
        parser.add_argument(
            "-f",
            "--format",
            type=str,
            choices=["dot", "analysis", "mermaid"],
            default="analysis",
            help="Output format (default: analysis)",
        )
        parser.add_argument(
            "-o",
            "--output",
            nargs="?",
            type=str,
            default=None,
            help="Output file path (required for dot format)",
        )
        parser.add_argument(
            "--use-cache",
            action="store_true",
            help="Use cached results if available (disabled by default)",
        )
        parser.add_argument(
            "--clear-cache",
            action="store_true",
            help="Invalidate all cached results before running",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Handle the command execution."""
        # Store output options
        self.output_format = options["format"]
        self.output_path = Path(options["output"]) if options.get("output") else None

        # Validate output path for dot format
        if self.output_format == "dot" and not self.output_path:
            self.stderr.write("Error: Output path is required for dot format")
            return

        # Get filtered model list
        model_list = get_model_list(
            filter_option=options["filter"],
            prefix=options.get("prefix"),
            exclude=options.get("exclude"),
            abstract=options.get("abstract"),
            proxy=options.get("proxy"),
        )

        if not model_list:
            self.stderr.write("No models found matching filters")
            return

        # Build graph
        try:
            graph = build_modelgraph(model_list)
        except Exception as e:
            self.stderr.write(f"Error building graph: {str(e)}")
            return

        # Handle output based on format
        output_formats = {
            "dot": DotOutputFormat(),
            "analysis": TextAnalysisOutputFormat(),
            "mermaid": MermaidOutputFormat(),
        }

        output_handler = output_formats[self.output_format]

        try:
            output_handler.output(graph, self.output_path)
            if self.output_path:
                self.stdout.write(self.style.SUCCESS(f"Output written to {self.output_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
