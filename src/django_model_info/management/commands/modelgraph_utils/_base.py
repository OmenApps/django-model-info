"""Base classes for graph output formats."""
import abc
from pathlib import Path
from typing import Optional

import networkx as nx


class GraphOutputFormat(abc.ABC):
    """Abstract base class for graph output formats."""

    @abc.abstractmethod
    def output(self, graph: nx.MultiDiGraph, output_path: Optional[Path] = None) -> None:
        """Output the graph in the specific format."""
