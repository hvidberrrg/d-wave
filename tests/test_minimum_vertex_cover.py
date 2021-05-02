import unittest
import dimod
import networkx as nx
import qubo.minimum_vertex_cover as mvc
from mock import patch


class MinimumVertexCoverTest(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 3), (1, 2), (1, 3), (4, 2), (4, 3)])
        self.min_vertex_cover = {0, 1, 4}
        self.min_vertex_cover_info = {0: 1, 1: 1, 2: 0, 3: 0, 4: 1}

    def test_generate_minimum_vertex_cover_bqm(self):
        expected_linear_biases = {0: -15.0, 1: -23.0, 3: -23.0, 2: -15.0, 4: -15.0}
        expected_quadratic_biases = {(0, 1): 8, (0, 3): 8, (1, 2): 8, (1, 3): 8, (3, 4): 8, (2, 4): 8}

        bqm = mvc.generate_minimum_vertex_cover_bqm(self.graph)
        self.assertEqual(bqm.linear, expected_linear_biases, "The linear biases of the BQM are not as expected")
        self.assertEqual(bqm.quadratic, expected_quadratic_biases, "The quadratic biases of the BQM are not as expected")

    def test_minimum_vertex_cover(self):
        # Patch LeapHybridSampler in the scope of the module it is imported into (i.e. sampler.py)
        with patch('qubo.sampler.LeapHybridSampler') as mock_lhs:
            # Build a mock sample set - https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/generated/dimod.SampleSet.from_samples.html
            mock_sampleset = dimod.SampleSet.from_samples([self.min_vertex_cover_info], dimod.BINARY, [1])
            mock_lhs_instance = mock_lhs.return_value
            mock_lhs_instance.sample.return_value = mock_sampleset

            min_cover = mvc.minimum_vertex_cover(self.graph)
            self.assertEqual(min_cover, self.min_vertex_cover, "The minimum vertex cover is not correct")

    def test_is_vertex_cover(self):
        is_cover = mvc.is_vertex_cover(self.graph, self.min_vertex_cover)
        self.assertTrue(is_cover, "Something went wrong - it is indeed a vertex cover!")
