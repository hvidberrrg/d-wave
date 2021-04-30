from __future__ import annotations
import dimod
import qubo.sampler as sampler


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


def partition_numbers(set_of_numbers: list[int]) -> tuple[list[int], list[int]]:
    """Solves the number partitioning problem for the supplied set of numbers

    Args:
        set_of_numbers (list[int]):
            A set of numbers, represented as a list to maintain ordering

    Returns:
            A tuple containing two subsets of numbers (represented as lists) that represents a solution to the
            number partitioning problem for the supplied 'set_of_numbers'
    """
    bqm = generate_partition_problem_bqm(set_of_numbers)
    sample_label = "Partition Problem (" + str(len(set_of_numbers)) + " numbers)"
    partitioning_info = sampler.sample_dwave(bqm, sample_label)
    assert (len(set_of_numbers) == len(partitioning_info)), "Something went wrong... the partitioning info doesn't match the set of input numbers."

    subset_of_numbers1: list[int] = list()
    subset_of_numbers2: list[int] = list()
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
