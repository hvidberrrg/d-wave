import unittest
import networkx as nx
import qubo.minimum_vertex_cover as mvc


class MinimumVertexCoverTest(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 3), (1, 2), (1, 3), (4, 2), (4, 3)])
        self.min_vertex_cover = {0, 1, 4}

    def test_is_vertex_cover(self):
        is_cover = mvc.is_vertex_cover(self.graph, self.min_vertex_cover)
        self.assertTrue(is_cover, "Something went wrong - it is indeed a vertex cover!")
