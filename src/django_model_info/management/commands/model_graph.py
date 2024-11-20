"""Django management command for generating model relationship graphs."""

import abc
from pathlib import Path
from typing import Optional

from django.apps import apps as django_apps
from django.core.management.base import BaseCommand, CommandParser

try:
    import networkx as nx
    import pydot
except ImportError as e:
    raise ImportError("The networkx and pydot packages are required for this command.") from e


class GraphOutputFormat(abc.ABC):
    """Abstract base class for graph output formats."""

    @abc.abstractmethod
    def output(self, graph: nx.MultiDiGraph, output_path: Optional[Path] = None) -> None:
        """Output the graph in the specific format."""


class DotOutputFormat(GraphOutputFormat):
    """Output graph in DOT format."""

    def output(self, graph: nx.MultiDiGraph, output_path: Optional[Path] = None) -> None:
        """Export the graph to DOT format."""
        if not output_path:
            raise ValueError("Output path is required for DOT format")

        # Add styling to edges
        G_vis = self._prepare_graph_for_visualization(graph)

        # Convert to pydot for more control over the output
        dot_graph = nx.drawing.nx_pydot.to_pydot(G_vis)

        # Add global graph attributes
        dot_graph.set_rankdir("LR")

        # Create legend subgraph
        legend = pydot.Cluster("legend", label="Legend", rankdir="LR")

        # Create the legend table nodes
        key_table = """<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
            <tr><td align="right" port="i1">OneToOneField </td></tr>
            <tr><td align="right" port="i2">OneToOneRel </td></tr>
            <tr><td align="right" port="i3">ForeignKey </td></tr>
            <tr><td align="right" port="i4">ManyToOneRel </td></tr>
            <tr><td align="right" port="i5">ManyToManyField </td></tr>
            <tr><td align="right" port="i6">ManyToManyRel </td></tr>
            </table>>"""

        spacer_table = """<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
            <tr><td port="i1">&nbsp;</td></tr>
            <tr><td port="i2">&nbsp;</td></tr>
            <tr><td port="i3">&nbsp;</td></tr>
            <tr><td port="i4">&nbsp;</td></tr>
            <tr><td port="i5">&nbsp;</td></tr>
            <tr><td port="i6">&nbsp;</td></tr>
            </table>>"""

        # Create and add the nodes
        key_node = pydot.Node("key", label=key_table, shape="plaintext")
        key2_node = pydot.Node("key2", label=spacer_table, shape="plaintext")
        legend.add_node(key_node)
        legend.add_node(key2_node)

        # Add the legend edges
        legend_edges = [
            ("key:i1:e", "key2:i1:w", {"color": "chartreuse4", "penwidth": "2.0"}),
            ("key:i2:e", "key2:i2:w", {"color": "chartreuse4", "style": "dashed"}),
            ("key:i3:e", "key2:i3:w", {"color": "blue", "penwidth": "2.0"}),
            ("key:i4:e", "key2:i4:w", {"color": "blue", "style": "dashed"}),
            ("key:i5:e", "key2:i5:w", {"color": "red", "penwidth": "2.0"}),
            ("key:i6:e", "key2:i6:w", {"color": "red", "style": "dashed"}),
        ]

        for src, dst, attrs in legend_edges:
            edge = pydot.Edge(src, dst, **attrs)
            legend.add_edge(edge)

        # Add the legend subgraph to the main graph
        dot_graph.add_subgraph(legend)

        # Write the graph to file
        dot_graph.write(output_path, format="dot")

    def _prepare_graph_for_visualization(self, G: nx.MultiDiGraph) -> nx.MultiDiGraph:
        """Prepare graph for visualization by adding styles."""
        styles = {
            "OneToOneField": {
                "color": "chartreuse4",
                "style": "solid",
                "penwidth": "2.0",
                "arrowhead": "normal",
                "direction": "forward",
            },
            "ForeignKey": {
                "color": "blue",
                "style": "solid",
                "penwidth": "2.0",
                "arrowhead": "normal",
                "direction": "forward",
            },
            "ManyToManyField": {
                "color": "red",
                "style": "solid",
                "penwidth": "2.0",
                "arrowhead": "normal",
                "direction": "forward",
            },
            "OneToOneRel": {
                "color": "chartreuse4",
                "style": "dashed",
                "penwidth": "1.0",
                "arrowhead": "normal",
                "direction": "back",
            },
            "ManyToOneRel": {
                "color": "blue",
                "style": "dashed",
                "penwidth": "1.0",
                "arrowhead": "normal",
                "direction": "back",
            },
            "ManyToManyRel": {
                "color": "red",
                "style": "dashed",
                "penwidth": "1.0",
                "arrowhead": "normal",
                "direction": "back",
            },
        }

        G_vis = G.copy()
        for u, v, key, data in G_vis.edges(data=True, keys=True):
            style = styles.get(data["relationship_type"], {})
            G_vis.edges[u, v, key].update(style)

            if data["direction"] == "forward":
                label = f"{data['relationship_type']}\n{data['field_name']}"
            else:
                label = f"{data['relationship_type']}\n(reverse: {data['field_name']})"
            G_vis.edges[u, v, key]["label"] = label

        return G_vis


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

        output.append("\nBasic Statistics:")
        output.append(f"  Models: {analysis['node_count']}")
        output.append(f"  Relationships: {analysis['edge_count']}")

        if analysis["isolated_models"]:
            output.append("\nIsolated Models:")
            for model in sorted(analysis["isolated_models"]):
                output.append(f"  - {model}")

        output.append("\nModel Relationships:")
        relationships_by_source = {}
        for rel_data in analysis["relationships"].values():
            source = rel_data["source"]
            if source not in relationships_by_source:
                relationships_by_source[source] = []
            relationships_by_source[source].append(rel_data)

        for source in sorted(relationships_by_source.keys()):
            output.append(f"\n  {source}:")
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


class Command(BaseCommand):
    """Django management command to generate model relationship graphs."""

    help = "Generate a graph showing relationships between models"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add command arguments."""
        parser.add_argument(
            "-f",
            "--filter",
            nargs="+",
            type=str,
            help="Limit to specific apps or models (format: appname or appname.ModelName)",
        )
        parser.add_argument(
            "--format",
            type=str,
            choices=["dot", "analysis"],
            default="analysis",
            help="Output format (default: analysis)",
        )
        parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="Output file path (required for dot format)",
        )

    def get_relationship_type(self, field) -> str:
        """Get the relationship type for a field."""
        if field.__class__.__name__ == "OneToOneField":
            return "OneToOneField"
        elif field.__class__.__name__ == "ForeignKey":
            return "ForeignKey"
        elif field.__class__.__name__ == "ManyToManyField":
            return "ManyToManyField"
        elif field.__class__.__name__ == "OneToOneRel":
            return "OneToOneRel"
        elif field.__class__.__name__ == "ManyToOneRel":
            return "ManyToOneRel"
        elif field.__class__.__name__ == "ManyToManyRel":
            return "ManyToManyRel"
        return "Unknown"

    def get_model_list(self, filter_option: Optional[list[str]] = None) -> list:
        """Get filtered or complete list of models."""
        if not filter_option:
            return sorted(django_apps.get_models(), key=lambda x: (x._meta.app_label, x._meta.object_name))

        model_list = []
        for filter_item in filter_option:
            if "." in filter_item:
                model = django_apps.get_model(filter_item)
                model_list.append(model)
            else:
                try:
                    app_models = django_apps.get_app_config(filter_item).get_models()
                    model_list.extend(app_models)
                except LookupError:
                    self.stderr.write(f"Unknown app: {filter_item}")

        return model_list

    def build_model_graph(self, model_list: list) -> nx.MultiDiGraph:
        """Build graph representing model relationships."""
        G = nx.MultiDiGraph()

        model_labels = {f"{model._meta.app_label}.{model._meta.model_name}" for model in model_list}

        # Add nodes
        for model in model_list:
            model_label = f"{model._meta.app_label}.{model._meta.model_name}"
            G.add_node(model_label, model=model)

        # Add edges
        for model in model_list:
            model_label = f"{model._meta.app_label}.{model._meta.model_name}"
            fields = model._meta.get_fields(include_hidden=True)

            for field in fields:
                if hasattr(field, "related_model") and field.related_model:
                    related_label = f"{field.related_model._meta.app_label}." f"{field.related_model._meta.model_name}"

                    if related_label in model_labels:
                        relationship_type = self.get_relationship_type(field)
                        direction = (
                            "forward"
                            if relationship_type in ("OneToOneField", "ForeignKey", "ManyToManyField")
                            else "reverse"
                        )

                        G.add_edge(
                            model_label,
                            related_label,
                            key=direction,
                            relationship_type=relationship_type,
                            field_name=field.name,
                            direction=direction,
                        )

        return G

    def handle(self, *args, **options) -> None:
        """Handle the command execution."""
        # Get models
        model_list = self.get_model_list(options["filter"])
        if not model_list:
            self.stderr.write("No models found")
            return

        # Build graph
        graph = self.build_model_graph(model_list)

        # Handle output
        output_formats = {
            "dot": DotOutputFormat(),
            "analysis": TextAnalysisOutputFormat(),
        }

        output_format = output_formats[options["format"]]
        output_path = Path(options["output"]) if options.get("output") else None

        try:
            output_format.output(graph, output_path)
            if output_path:
                self.stdout.write(self.style.SUCCESS(f"Output written to {output_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
