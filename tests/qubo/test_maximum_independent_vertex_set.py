import unittest
import dimod
import networkx as nx
import qubo.maximum_independent_vertex_set as mivs
from mock import patch


class MaximumIndependentVertexSetTest(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 3), (1, 2), (1, 3), (4, 2), (4, 3)])
        self.min_vertex_cover = {0, 1, 4}
        self.max_independent_set = {2, 3}
        self.min_vertex_cover_info = {0: 1, 1: 1, 2: 0, 3: 0, 4: 1}

    def test_maximum_independent_vertex_set(self):
        # Patch LeapHybridSampler in the scope of the module it is imported into (i.e. sampler.py)
        with patch('qubo.sampler.LeapHybridSampler') as mock_lhs:
            # Build a mock sample set - https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/generated/dimod.SampleSet.from_samples.html
            mock_sampleset = dimod.SampleSet.from_samples([self.min_vertex_cover_info], dimod.BINARY, [1])
            mock_lhs_instance = mock_lhs.return_value
            mock_lhs_instance.sample.return_value = mock_sampleset

            maximum_independent_set = mivs.maximum_independent_vertex_set(self.graph)
            self.assertEqual(maximum_independent_set, self.max_independent_set, "The maximum independent vertex set is not correct")

    def test_is_vertex_cover(self):
        is_independent_set = mivs.is_independent_vertex_set(self.graph, self.max_independent_set)
        self.assertTrue(is_independent_set, "Something went wrong - it is indeed an independent vertex set!")

    def test_is_vertex_cover_false(self):
        is_independent_set = mivs.is_independent_vertex_set(self.graph, self.min_vertex_cover)
        self.assertFalse(is_independent_set, "Something went wrong - it is not an independent vertex set!")
