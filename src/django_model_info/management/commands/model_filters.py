"""Django management command to display model field relationships."""
import hashlib
import json
import logging
from io import StringIO
from pathlib import Path
from typing import Any, Optional

from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser
from rich.console import Console
from rich.table import Table

from .common_utils._cache import cache, get_cache_version, increment_cache_version
from .common_utils._settings import (
    CACHE_ALWAYS,
    CACHE_ENABLED,
    CACHE_KEY_PREFIX,
    CACHE_TIMEOUT,
)
from .model_filters_utils._field_utils import get_model_from_input, get_ordered_fields

logger = logging.getLogger(__name__)

console = Console(record=True)


def get_cache_key(model: Any, options: dict[str, Any]) -> str:
    """Generate a cache key based on model and options."""
    # Create a dictionary of relevant options for the cache key
    key_data = {
        "model": model._meta.label,
        "max_depth": options.get("max_depth"),
        "max_paths": options.get("max_paths"),
        "exclude": options.get("exclude"),
        "field_type": options.get("field_type"),
        "target_model": options.get("target_model"),
        "target_field": options.get("target_field"),
        "version": get_cache_version(),  # Include cache version in key
    }

    # Convert to a stable string representation and hash it
    key_str = json.dumps(key_data, sort_keys=True)
    key_hash = hashlib.md5(key_str.encode()).hexdigest()

    return f"{CACHE_KEY_PREFIX}{key_hash}"

class Command(BaseCommand):
    """Display model field relationships in tabular format."""

    help = "Display model field relationships in tabular or markdown format"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.export_option = None

    def get_options(self, options) -> tuple:
        """Get verbosity, filter, and export options."""
        export_option = (
            options.get("output")
            if options.get("output", None) is not None and isinstance(options.get("output"), str)
            else None
        )

        return export_option

    def add_arguments(self, parser: CommandParser) -> None:
        """Add command arguments."""
        parser.add_argument(
            "filter",
            nargs="+",
            type=str,
            help="App, model or app.Model to analyze",
        )
        parser.add_argument(
            "--target-model",
            nargs="+",
            type=str,
            help="Filter to fields related to these models",
        )
        parser.add_argument(
            "--target-field",
            nargs="+",
            type=str,
            help="Filter to specific field names",
        )
        parser.add_argument(
            "--by-depth",
            action="store_true",
            help="Sort by number of relationship traversals",
        )
        parser.add_argument(
            "--by-model",
            action="store_true",
            help="Sort by related model name",
        )
        parser.add_argument(
            "-o",
            "--output",
            nargs="?",
            type=str,
            default=None,
            help="Filename to export. Extension must be .txt, .html, .htm, or .md",
        )
        parser.add_argument(
            "-m",
            "--markdown",
            action="store_true",
            help="Output in markdown format",
        )
        # New arguments
        parser.add_argument(
            "--max-depth",
            type=int,
            default=4,
            help="Maximum number of relationship traversals",
        )
        parser.add_argument(
            "--max-paths",
            type=int,
            help="Maximum number of paths to return",
        )
        parser.add_argument(
            "-e",
            "--exclude",
            nargs="+",
            type=str,
            help="Apps, models, or fields to exclude",
        )
        parser.add_argument(
            "--prefix",
            type=str,
            help="Include only models/fields with this prefix",
        )
        parser.add_argument(
            "--field-type",
            type=str,
            help="Filter by field type (e.g., IntegerField, CharField)",
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
        """Execute command."""
        # Clear cache if requested using version invalidation
        if options["clear_cache"]:
            increment_cache_version(self)
            if not options.get("filter"):  # If only clearing cache
                return

        self.export_option = self.get_options(options)

        models = self.get_filtered_models(options["filter"])

        if not models:
            self.stderr.write("No models found matching filters")
            return

        for model in sorted(models, key=lambda x: x._meta.label):
            data = self.get_table_data(model, options)

            if options["markdown"]:
                self.print_markdown(model, data)
            else:
                self.print_table(model, data)

        total = sum(len(self.get_table_data(m, options)) for m in models)

        if options["markdown"]:
            print(f"\n**Total Fields: {total}**")
        else:
            console.print(f"\nTotal Fields: {total}", style="bold green")

        if self.export_option:
            self.export_results(models, options)

    def get_filtered_models(self, filters: Optional[list[str]], prefix: Optional[str] = None) -> list[Any]:
        """Get models based on filter arguments."""
        models = []

        if not filters:
            all_models = apps.get_models()
            if prefix:
                return [m for m in all_models if m.__name__.startswith(prefix)]
            return all_models

        for filter_item in filters:
            if prefix and not any(m.__name__.startswith(prefix) for m in apps.get_models()):
                continue

            model = get_model_from_input(filter_item)
            if model:
                if not prefix or model.__name__.startswith(prefix):
                    models.append(model)
            else:
                try:
                    app_config = apps.get_app_config(filter_item)
                    app_models = app_config.get_models()
                    if prefix:
                        app_models = [m for m in app_models if m.__name__.startswith(prefix)]
                    models.extend(app_models)
                except LookupError:
                    self.stderr.write(f"Invalid filter: {filter_item}")

        return list(set(models))

    def process_exclude_patterns(self, excludes: list[str]) -> list[str]:
        """Process exclude patterns to handle both app and model exclusions.

        Examples:
            - 'Permission' -> ['Permission']
            - 'auth.Permission' -> ['auth.Permission']
            - 'auth' -> ['User', 'Group', 'Permission', ...]  (all auth models)
        """
        if not excludes:
            return []

        processed_excludes = []
        for pattern in excludes:
            # Case 1: app.Model pattern - keep as is
            if "." in pattern and not pattern.endswith("."):
                processed_excludes.append(pattern)
            # Case 2: app only - expand to all models in app
            elif not "." in pattern:
                # First check if it's an app name
                try:
                    app_config = apps.get_app_config(pattern)
                    app_models = [f"{pattern}.{model.__name__}" for model in app_config.get_models()]
                    processed_excludes.extend(app_models)
                except LookupError:
                    # Not an app name, treat as model name
                    processed_excludes.append(pattern)

        return list(set(processed_excludes))

    def get_table_data(self, model: Any, options: dict[str, Any]) -> list[list[str]]:
        """Get field data for a model."""
        if CACHE_ENABLED:
            if options.get("use_cache") or CACHE_ALWAYS:
                cache_key = get_cache_key(model, options)
                cached_data = cache.get(cache_key)
                if cached_data is not None:
                    return cached_data

        # Process multiple target models
        target_models = []
        if options.get("target_model"):
            target_models = [
                get_model_from_input(target)
                for target in options["target_model"]
                if get_model_from_input(target) is not None
            ]

        # Process exclude patterns
        processed_excludes = self.process_exclude_patterns(options.get("exclude", []))

        # Get all field data for each target model
        all_data = []
        if target_models:
            for target_model in target_models:
                data = get_ordered_fields(
                    model,
                    by_depth=options["by_depth"],
                    by_model=options["by_model"],
                    target_model=target_model,
                    target_field=options.get("target_field"),
                    max_depth=options["max_depth"],
                    max_paths=options["max_paths"],
                    excludes=processed_excludes,
                    field_type=options.get("field_type"),
                )
                all_data.extend(data)
        else:
            all_data = get_ordered_fields(
                model,
                by_depth=options["by_depth"],
                by_model=options["by_model"],
                target_model=None,
                target_field=options.get("target_field"),
                max_depth=options["max_depth"],
                max_paths=options["max_paths"],
                excludes=processed_excludes,
                field_type=options.get("field_type"),
            )

        # Apply prefix filter if specified
        if options.get("prefix"):
            all_data = [
                row
                for row in all_data
                if any(part.startswith(options["prefix"].lower()) for part in row[0].split("__"))
            ]

        if CACHE_ENABLED:
            if options.get("use_cache") or CACHE_ALWAYS:
                cache.set(cache_key, all_data, CACHE_TIMEOUT)

        return all_data

    def print_markdown(self, model: Any, data: list[list[str]]) -> None:
        """Print table in markdown format."""
        if not data:
            return

        print(f"\n## {model._meta.label}")
        print("\n| Field Path | Model | Field Name | Field Type | Models in Path |")
        print("|------------|-------|------------|------------|----------------|")
        for row in data:
            print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")

    def export_markdown(self, models: list, options: dict[str, Any]) -> str:
        """Export markdown content."""
        output = StringIO()
        for model in models:
            data = self.get_table_data(model, options)
            if data:
                output.write(f"\n## {model._meta.label}\n")
                output.write("\n| Field Path | Model | Field Name | Field Type | Models in Path |\n")
                output.write("|------------|-------|------------|------------|----------------|\n")
                for row in data:
                    output.write(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |\n")
        return output.getvalue()

    def print_table(self, model: Any, data: list[list[str]]) -> None:
        """Print table using rich."""
        if not data:
            return

        table = Table(title=model._meta.label)

        table.add_column("Field Path", style="cyan")
        table.add_column("Model", style="yellow")
        table.add_column("Field Name", style="green")
        table.add_column("Field Type", style="magenta")
        table.add_column("Models in Path", style="blue")

        for row in data:
            table.add_row(*row)

        console.print(table)
        console.print("")

    def export_results(self, models=None, options=None):
        """Handle export functionality."""
        extension = Path(self.export_option).suffix
        if extension in [".html", ".htm"]:
            console.save_html(path=self.export_option)
        elif extension == ".txt":
            console.save_text(path=self.export_option)
        elif extension == ".md":
            md_content = self.export_markdown(models, options)
            with open(self.export_option, "w", encoding="utf-8") as f:
                f.write(md_content)
