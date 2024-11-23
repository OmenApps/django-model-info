"""DOT format output for model graphs."""
from pathlib import Path
from typing import Optional

import networkx as nx
import pydot

from ._base import GraphOutputFormat


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
        dot_graph.set_rankdir("LR")

        # Add legend
        self._add_legend(dot_graph)

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

    def _add_legend(self, dot_graph: pydot.Dot) -> None:
        """Add a legend to the graph."""
        legend = pydot.Cluster("legend", label="Legend", rankdir="LR")

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

        key_node = pydot.Node("key", label=key_table, shape="plaintext")
        key2_node = pydot.Node("key2", label=spacer_table, shape="plaintext")
        legend.add_node(key_node)
        legend.add_node(key2_node)

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

        dot_graph.add_subgraph(legend)
