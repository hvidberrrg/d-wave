import unittest
import dimod
import qubo.partition_problem as pp
from mock import patch


class PartitionProblemTest(unittest.TestCase):

    def setUp(self):
        self.set_of_numbers = [25, 7, 13, 31, 42, 17, 21, 10]
        self.subset1 = [7, 13, 42, 21]
        self.subset2 = [25, 31, 17, 10]
        self.partitioning_info = {0: 0, 1: 1, 2: 1, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0}

    def test_generate_partition_problem_bqm(self):
        expected_linear_biases = {0: -3525.0, 1: -1113.0, 2: -1989.0, 3: -4185.0, 4: -5208.0, 5: -2533.0, 6: -3045.0, 7: -1560.0}
        expected_quadratic_biases = {(0, 1): 350, (0, 2): 650, (0, 3): 1550, (0, 4): 2100, (0, 5): 850,  (0, 6): 1050, (0, 7): 500, 
                                                  (1, 2): 182, (1, 3): 434,  (1, 4): 588,  (1, 5): 238,  (1, 6): 294,  (1, 7): 140, 
                                                               (2, 3): 806,  (2, 4): 1092, (2, 5): 442,  (2, 6): 546,  (2, 7): 260, 
                                                                             (3, 4): 2604, (3, 5): 1054, (3, 6): 1302, (3, 7): 620, 
                                                                                           (4, 5): 1428, (4, 6): 1764, (4, 7): 840, 
                                                                                                         (5, 6): 714,  (5, 7): 340, 
                                                                                                                       (6, 7): 420}
        bqm = pp.generate_partition_problem_bqm(self.set_of_numbers)
        self.assertEqual(bqm.linear, expected_linear_biases, "The linear biases of the BQM are not as expected")
        self.assertEqual(bqm.quadratic, expected_quadratic_biases, "The quadratic biases of the BQM are not as expected")

    def test_partition_numbers(self):    
        # Patch LeapHybridSampler in the scope of the module it is imported into (i.e. sampler.py)
        with patch('qubo.sampler.LeapHybridSampler') as mock_lhs:  
            # Build a mock sample set - https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/generated/dimod.SampleSet.from_samples.html    
            mock_sampleset = dimod.SampleSet.from_samples([self.partitioning_info], dimod.BINARY, [1])
            mock_lhs_instance = mock_lhs.return_value
            mock_lhs_instance.sample.return_value = mock_sampleset

            s1, s2 = pp.partition_numbers(self.set_of_numbers)
            self.assertEqual(s1, self.subset1, "The partitioning failed")
            self.assertEqual(s2, self.subset2, "The partitioning failed")

    def test_perfectness(self):
        p = pp.perfectness(self.subset1, self.subset2)
        self.assertEqual(p, 0, "Expected a perfect partition")
