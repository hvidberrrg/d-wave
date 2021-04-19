from __future__ import annotations
import dimod
from dwave.system import LeapHybridSampler


def generate_partition_problem_bqm(set_of_numbers: list[int]) -> dimod.BinaryQuadraticModel:
    """Generates an instance of BinaryQuadraticModel with a QUBO formulation of the number partitioning
    problem for the set of numbers, given as argument.

    The implementation is based on Fred Glover et al: "Quantum Bridge Analytics I: A Tutorial on Formulating 
    and Using QUBO Models", arXiv:1811.11538

    Args:
        set_of_numbers (list[int]):
            A set of numbers, represented as a list to maintain ordering
    
    Returns:
            An instance of BinaryQuadraticModel with a QUBO formulation of the number partitioning
            problem for 'set_of_numbers'.
    """
    linear: dict[int, int] = dict()
    quadratic: dict[tuple[int, int], int] = dict()
    sum_of_numbers = sum(set_of_numbers)
    for i in range(len(set_of_numbers)):
        linear[i] = set_of_numbers[i]*(set_of_numbers[i] - sum_of_numbers)
        for j in range(1 + i, len(set_of_numbers)):
            quadratic[(i, j)] = 2*set_of_numbers[i]*set_of_numbers[j]
    
    offset = 0.0
    vartype = dimod.BINARY
    return dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)


def sample_dwave(bqm: dimod.BinaryQuadraticModel, sample_label: str) -> dict[int, int]:
    """Ask the DWave sampler to return the best sample for the supplied binary quadratic model
    
    Args:
        bqm (dimod.BinaryQuadraticModel):
            Binary qudratic model representing the problem
        sample_label (str):
            Label to use for the sample - appears in the DWave dashboard

        Returns:
            A dictionary mapping the location of each element in the input "vector" to the
            corresponding 0/1 value returned by the sampler
    """
    sampler = LeapHybridSampler()
    sample_set = sampler.sample(bqm, label = sample_label)
    return sample_set.first.sample


def partition_numbers(set_of_numbers: list[int]) -> tuple[list[int], list[int]]:
    """Solves the number partitioning problem for the supplied set of numbers

    Args:
        set_of_numbers (list[int]):
            A set of numbers, represented as a list to maintain ordering
    
    Returns:
            A tuple containing to subsets of numbers (represented as lists) that represents a solution to the
            number partitioning problem for the supplied 'set_of_numbers'
    """
    subset_of_numbers1: list[int] = list()
    subset_of_numbers2: list[int] = list()
    bqm = generate_partition_problem_bqm(set_of_numbers)
    sample_label = "Partition Problem (" + str(len(set_of_numbers)) + " numbers)"
    partitioning_info = sample_dwave(bqm, sample_label)
    for i in range(len(partitioning_info)):
        if partitioning_info[i] == 1:
            subset_of_numbers1.append(set_of_numbers[i]) 
        else:
            subset_of_numbers2.append(set_of_numbers[i])
    
    return subset_of_numbers1, subset_of_numbers2


def perfectness(subset_of_numbers1: list[int], subset_of_numbers2: list[int]) -> int:
    """Calculates the 'perfectness' of the partitioning. A value of '0' indicates a perfect partition.

    Args:
        subset_of_numbers1 (list[int]):
            A set of numbers
        subset_of_numbers2 (list[int]):
            A set of numbers
    
    Returns:
            The absolute value of the difference of the sums of the numbers in the two subsets
    """
    return abs(sum(subset_of_numbers1) - sum(subset_of_numbers2))


def main():
    #s = [4, 2, 7, 1]
    #s = [25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1]
    set_of_numbers = [25, 7, 13, 31, 42, 17, 21, 10] # The set of numbers is represented as a list to maintain ordering
    subset_of_numbers1, subset_of_numbers2 = partition_numbers(set_of_numbers)

    print(subset_of_numbers1)
    print(subset_of_numbers2)
    print("Perfectness: " + str(perfectness(subset_of_numbers1, subset_of_numbers2)))


main()