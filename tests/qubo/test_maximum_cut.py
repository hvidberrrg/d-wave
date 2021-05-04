import unittest
import dimod
import networkx as nx
import qubo.maximum_cut as mc
from mock import patch


class MaximumCutTest(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 3), (1, 2), (1, 3), (4, 2), (4, 3)])
        self.maximum_cut_info = {0: 0, 1: 1, 2: 0, 3: 0, 4: 1}

    def test_generate_maximum_cut_bqm(self):
        expected_linear_biases = {0: -2, 1: -3, 3: -3, 2: -2, 4: -2}
        expected_quadratic_biases = {(0, 1): 2, (0, 3): 2, (1, 3): 2, (1, 2): 2, (3, 4): 2, (2, 4): 2}

        bqm = mc.generate_maximum_cut_bqm(self.graph)
        self.assertEqual(bqm.linear, expected_linear_biases, "The linear biases of the BQM are not as expected")
        self.assertEqual(bqm.quadratic, expected_quadratic_biases, "The quadratic biases of the BQM are not as expected")

    def test_maximum_cut(self):
        # Patch LeapHybridSampler in the scope of the module it is imported into (i.e. sampler.py)
        with patch('qubo.sampler.LeapHybridSampler') as mock_lhs:
            # Build a mock sample set - https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/generated/dimod.SampleSet.from_samples.html
            mock_sampleset = dimod.SampleSet.from_samples([self.maximum_cut_info], dimod.BINARY, [1])
            mock_lhs_instance = mock_lhs.return_value
            mock_lhs_instance.sample.return_value = mock_sampleset

            nodes_set1, nodes_set2, cut_edges, uncut_edges = mc.maximum_cut(self.graph)
            self.assertEqual(len(nodes_set1), 2, "Node set 1 is the wrong size")
            self.assertTrue(1 in nodes_set1, "Node 1 should be in set0")
            self.assertTrue(4 in nodes_set1, "Node 4 should be in set0")
            self.assertEqual(len(nodes_set2), 3, "Node set 2 is the wrong size")
            self.assertTrue(0 in nodes_set2, "Node 0 should be in set1")
            self.assertTrue(2 in nodes_set2, "Node 2 should be in set1")
            self.assertTrue(3 in nodes_set2, "Node 3 should be in set1")
            self.assertEqual(len(cut_edges), 5, "The set of cut edges is the wrong size")
            self.assertTrue((0, 1) in cut_edges, "Edge (0, 1) should be in the set of cut edges")
            self.assertTrue((1, 2) in cut_edges, "Edge (1, 2) should be in the set of cut edges")
            self.assertTrue((1, 3) in cut_edges, "Edge (1, 3) should be in the set of cut edges")
            self.assertTrue((3, 4) in cut_edges, "Edge (3, 4) should be in the set of cut edges")
            self.assertTrue((2, 4) in cut_edges, "Edge (2, 4) should be in the set of cut edges")
            self.assertEqual(len(uncut_edges), 1, "The set of uncut edges is the wrong size")
            self.assertTrue((0, 3) in uncut_edges, "Edge (0, 3) should be in the set of uncut edges")
