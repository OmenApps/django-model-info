"""Mermaid format output for model graphs."""
from pathlib import Path
from typing import Optional

import networkx as nx

from ._base import GraphOutputFormat


class MermaidOutputFormat(GraphOutputFormat):
    """Output graph in Mermaid format."""

    def output(self, graph: nx.MultiDiGraph, output_path: Optional[Path] = None) -> None:
        """Export the graph to Mermaid format."""
        mermaid_content = self._generate_mermaid(graph)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(mermaid_content)
        else:
            print(mermaid_content)

    def _generate_mermaid(self, G: nx.MultiDiGraph) -> str:
        """Generate Mermaid diagram content."""
        lines = ["graph LR"]

        # Track processed relationships to avoid duplicates
        processed_relationships = set()

        # Add relationships with styling
        for u, v, key, data in G.edges(data=True, keys=True):
            # Create unique identifier for this relationship
            rel_id = (u, v, data["field_name"])
            if rel_id in processed_relationships:
                continue
            processed_relationships.add(rel_id)

            # Clean node names for Mermaid (replace dots with underscores)
            source = u.replace(".", "_")
            target = v.replace(".", "_")

            # Get relationship style
            line_start, line_end = self._get_relationship_style(data["relationship_type"], data["direction"])

            # Build relationship line with label
            if data["direction"] == "forward":
                label = f"{data['relationship_type']}<br>{data['field_name']}"
            else:
                label = f"{data['relationship_type']}<br>reverse: {data['field_name']}"

            # Add the relationship line with style and label
            lines.append(f'    {source}{line_start}"{label}"{line_end}{target}')

            # Add node definitions
            lines.append(f'    {source}["{u}"]')
            lines.append(f'    {target}["{v}"]')

        return "\n".join(lines)

    def _get_relationship_style(self, relationship_type: str, direction: str) -> tuple[str, str]:
        """Get Mermaid arrow style for relationship type.

        Returns:
            tuple[str, str]: The start and end parts of the line style
        """
        styles = {
            "OneToOneField": {"forward": ("==", "==="), "reverse": ("-.", ".->,")},
            "ForeignKey": {"forward": ("==", "==="), "reverse": ("-.", ".->,")},
            "ManyToManyField": {"forward": ("==", "==="), "reverse": ("-.", ".->,")},
            "OneToOneRel": {"forward": ("-.", ".->"), "reverse": ("-.", ".->")},
            "ManyToOneRel": {"forward": ("-.", ".->"), "reverse": ("-.", ".->")},
            "ManyToManyRel": {"forward": ("-.", ".->"), "reverse": ("-.", ".->")},
        }

        # Get the style or use default if not found
        style = styles.get(relationship_type, {}).get(direction, ("--", "-->"))
        return f"{style[0]} ", f" {style[1]}"
