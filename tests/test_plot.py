import unittest
import networkx as nx
import os as os
import pathlib as pl
import plot as plot


class PlotTest(unittest.TestCase):

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_maximum_cut(self):
        graph = nx.Graph()
        graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])
        nodes_set1 = {1, 4}
        nodes_set2 = {0, 2, 3}
        cut_edges = {(0, 1), (1, 2), (1, 3), (3, 4), (2, 4)}
        uncut_edges = {(0, 3)}
        filename = "test_maximum_cut.png"

        plot.maximum_cut(graph, nodes_set1, nodes_set2, cut_edges, uncut_edges, filename)
        self.assertIsFile(filename)
        os.remove(filename)

    def test_graph_with_colored_node_subset(self):
        graph = nx.Graph()
        graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])
        node_subset = {1, 2, 3}
        filename = "test_graph_with_colored_node_subset.png"

        plot.graph_with_colored_node_subset(graph, node_subset, filename)
        self.assertIsFile(filename)
        os.remove(filename)
