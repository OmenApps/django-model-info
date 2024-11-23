"""Analysis format output for model graphs."""
from pathlib import Path
from typing import Optional

import networkx as nx

from ._base import GraphOutputFormat


class TextAnalysisOutputFormat(GraphOutputFormat):
    """Output graph analysis in text format."""

    def output(self, graph: nx.MultiDiGraph, output_path: Optional[Path] = None) -> None:
        """Output graph analysis to console or file."""
        analysis = self._analyze_graph(graph)
        formatted_output = self._format_analysis(analysis)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(formatted_output)
        else:
            print(formatted_output)

    def _analyze_graph(self, G: nx.MultiDiGraph) -> dict:
        """Analyze the model multigraph."""
        try:
            analysis = {
                "node_count": G.number_of_nodes(),
                "edge_count": G.number_of_edges(),
                "isolated_models": list(nx.isolates(G)),
                "cycles": list(nx.simple_cycles(G)),
                "relationships": {},
                "degree_centrality": nx.degree_centrality(G),
                "in_degree_centrality": nx.in_degree_centrality(G),
                "out_degree_centrality": nx.out_degree_centrality(G),
                "strongly_connected_components": list(nx.strongly_connected_components(G)),
            }

            for u, v, key, data in G.edges(data=True, keys=True):
                rel_id = (u, v, data["direction"])
                analysis["relationships"][rel_id] = {
                    "source": u,
                    "target": v,
                    "type": data["relationship_type"],
                    "field_name": data["field_name"],
                    "direction": data["direction"],
                }

            return analysis

        except Exception as e:
            raise ValueError(f"Error analyzing graph: {str(e)}") from e

    def _format_analysis(self, analysis: dict) -> str:
        """Format the analysis results for display."""
        output = []
        output.append("Model Graph Analysis")
        output.append("===================")

        # Basic Statistics
        output.append("\nBasic Statistics:")
        output.append(f"  Models: {analysis['node_count']}")
        output.append(f"  Relationships: {analysis['edge_count']}")

        # Strongly Connected Components (if any non-singleton components exist)
        non_singleton_components = [comp for comp in analysis["strongly_connected_components"] if len(comp) > 1]
        if non_singleton_components:
            output.append("\nStrongly Connected Components (each model can reach all others):")
            for i, component in enumerate(non_singleton_components, 1):
                output.append(f"  Component {i}:")
                for model in sorted(component):
                    output.append(f"    - {model}")

        # Isolated Models
        if analysis["isolated_models"]:
            output.append("\nIsolated Models (no relationships to other models):")
            for model in sorted(analysis["isolated_models"]):
                output.append(f"    - {model}")

        # Centrality Metrics (show only if there are relationships)
        if analysis["edge_count"] > 0:
            output.append("\nCentrality Analysis (higher values indicate more connected models):")

            # Sort models by degree centrality for consistent output
            sorted_models = sorted(
                analysis["degree_centrality"].keys(), key=lambda x: (-analysis["degree_centrality"][x], x)
            )

            for model in sorted_models:
                if (
                    analysis["degree_centrality"][model] > 0
                    or analysis["in_degree_centrality"][model] > 0
                    or analysis["out_degree_centrality"][model] > 0
                ):
                    output.append(f"  {model}:")
                    output.append(f"    Overall Centrality: {analysis['degree_centrality'][model]:.3f}")
                    output.append(f"    Incoming: {analysis['in_degree_centrality'][model]:.3f}")
                    output.append(f"    Outgoing: {analysis['out_degree_centrality'][model]:.3f}")

        # Cycles (if any)
        if analysis["cycles"]:
            output.append("\nCycles Detected (models involved in circular relationships):")
            for cycle in analysis["cycles"]:
                output.append(f"  - {' -> '.join(cycle)} -> {cycle[0]}")

        # Model Relationships
        output.append("\nModel Relationships:")
        relationships_by_source = {}
        for rel_data in analysis["relationships"].values():
            source = rel_data["source"]
            if source not in relationships_by_source:
                relationships_by_source[source] = []
            relationships_by_source[source].append(rel_data)

        for source in sorted(relationships_by_source.keys()):
            output.append(f"  {source}:")
            for rel in sorted(relationships_by_source[source], key=lambda x: (x["target"], x["direction"])):
                direction_symbol = "→" if rel["direction"] == "forward" else "←"
                relationship_desc = (
                    f"{rel['type']} ({rel['field_name']})"
                    if rel["direction"] == "forward"
                    else f"{rel['type']} (reverse: {rel['field_name']})"
                )
                output.append(f"    {direction_symbol} {rel['target']}")
                output.append(f"      {relationship_desc}")

        return "\n".join(output)
