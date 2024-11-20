"""Markdown export functionality for Django model documentation."""

from dataclasses import dataclass
from typing import Any, Optional

from ._common_utils import clean_docstring


@dataclass
class MarkdownSection:
    """Represents a section in the markdown document."""

    title: str
    content: list[str]
    level: int = 1

    def render(self) -> str:
        """Render the section with proper markdown formatting."""
        header = f"{'#' * self.level} {self.title}\n"
        content = "\n".join(self.content)
        return f"{header}\n{content}\n"


class MarkdownTable:
    """Represents a markdown table with headers and rows."""

    def __init__(self, headers: list[str]):
        self.headers = headers
        self.rows: list[list[str]] = []

    def add_row(self, row: list[str]):
        """Add a row to the table."""
        self.rows.append(row)

    def render(self) -> str:
        """Render the table in markdown format."""
        if not self.headers:
            return ""

        table_lines = [
            "| " + " | ".join(self.headers) + " |",
            "|" + "|".join("-" * len(header) for header in self.headers) + "|",
        ]

        for row in self.rows:
            table_lines.append("| " + " | ".join(str(cell) for cell in row) + " |")

        return "\n".join(table_lines)


class MarkdownExporter:
    """Handles the generation of markdown documentation for Django models."""

    def __init__(self, verbosity: int, exclude_defaults: bool):
        self.verbosity = verbosity
        self.exclude_defaults = exclude_defaults

    def format_model_info_table(self, model_info: Any) -> MarkdownTable:
        """Format model information into a markdown table."""
        table = MarkdownTable(["Key", "Value"])
        for row in model_info.render_rows(19):
            if row[1]:  # Only add rows with values
                table.add_row([row[0], row[1]])
        return table

    def format_fields_table(self, fields: list[Any], field_type: str) -> Optional[MarkdownTable]:
        """Format field information into a markdown table."""
        if not fields:
            return None

        if self.verbosity >= 2:
            if field_type == "other":
                headers = ["Field Name", "Field Type", "Database Column", "Database Type", "Verbose Name"]
            elif field_type == "relation":
                headers = [
                    "Field Name",
                    "Field Type",
                    "Database Column",
                    "Database Type",
                    "Related Model",
                    "Related Name",
                ]
            else:
                return None
        else:
            headers = ["Field Name"]

        table = MarkdownTable(headers)

        for field in sorted(fields, key=lambda x: x.name):
            if self.verbosity >= 2:
                if field_type == "other":
                    row = [
                        f"`{field.name}`",
                        field.field_type,
                        field.field_column,
                        field.field_db_type,
                        field.field_verbose_name,
                    ]
                # elif field_type == "relation":
                else:
                    row = [
                        f"`{field.name}`",
                        field.field_type,
                        field.field_column,
                        field.field_db_type,
                        field.related_model,
                        field.related_name,
                    ]
            else:
                row = [f"`{field.name}`"]
            table.add_row(row)

        return table

    def format_methods_section(self, methods: tuple, method_types: list[str]) -> list[MarkdownSection]:
        """Format method information into markdown sections."""
        sections = []

        for method_type, method_list in zip(method_types, methods):
            if not method_list:
                continue

            headers = ["Method Name"]
            if self.verbosity >= 2:
                headers.append("Signature")
            if self.verbosity >= 3:
                headers.extend(["Docstring", "File", "Line Number"])

            table = MarkdownTable(headers)

            for method in sorted(method_list, key=lambda x: x.name):
                row = [f"`{method.name}`"]
                if self.verbosity >= 2:
                    row.append(f"`{method.signature}`" if method.signature else "")
                if self.verbosity >= 3:
                    row.extend(
                        [
                            clean_docstring(method.docstring) if method.docstring else "",
                            method.file if method.file else "",
                            str(method.line_number) if method.line_number else "",
                        ]
                    )
                table.add_row(row)

            section = MarkdownSection(title=f"{method_type} Methods", content=[table.render()], level=3)
            sections.append(section)

        return sections

    def format_managers_section(self, managers_info: dict) -> Optional[MarkdownSection]:
        """Format manager information into a markdown section."""
        if not managers_info or self.verbosity <= 1:
            return None

        content = []
        for manager_name, manager_info in managers_info.items():
            content.extend([f"### {manager_name}\n", f"**Class:** `{manager_info['name']}`\n"])

            if self.verbosity > 2 and manager_info["module"]:
                content.append(f"**Module:** `{manager_info['module']}`\n")

            if manager_info["docstring"]:
                content.append(f"*{manager_info['docstring']}*\n")

            if manager_info["methods"]:
                content.append("#### Custom Methods\n")
                for method_name, method_info in manager_info["methods"].items():
                    content.extend(
                        [
                            f"##### `{method_name}{method_info['signature']}`\n",
                            f"*{method_info['docstring']}*\n" if method_info["docstring"] else "",
                        ]
                    )

            self._add_queryset_info(content, manager_info)

        return MarkdownSection(title="Custom Managers", content=content, level=2)

    def _add_queryset_info(self, content: list[str], manager_info: dict):
        """Add queryset information to the managers section content."""
        if "queryset" not in manager_info:
            return

        queryset_info = manager_info["queryset"]
        content.extend(["#### Custom QuerySet\n", f"**Class:** `{queryset_info['name']}`\n"])

        if self.verbosity > 2 and queryset_info["module"]:
            content.append(f"**Module:** `{queryset_info['module']}`\n")

        if queryset_info["docstring"]:
            content.append(f"*{queryset_info['docstring']}*\n")

        if queryset_info["methods"]:
            content.append("##### Custom Methods\n")
            for method_name, method_info in queryset_info["methods"].items():
                method_content = [f"###### `{method_name}{method_info['signature']}`\n"]
                if method_info["docstring"]:
                    method_content.append(f"*{method_info['docstring']}*\n")
                if self.verbosity > 2 and method_info["source_file"] and method_info["line_number"]:
                    method_content.append(
                        f"Defined in: `{method_info['source_file']}`:`{method_info['line_number']}`\n"
                    )
                content.extend(method_content)
