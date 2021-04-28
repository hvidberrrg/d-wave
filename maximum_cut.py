from __future__ import annotations
from collections import defaultdict
import dimod
import networkx as nx
import sampler


def generate_maximum_cut_bqm(graph: nx.Graph) -> dimod.BinaryQuadraticModel:
    """Generates an instance of BinaryQuadraticModel with a QUBO formulation of the maximum cut
    for the graph given as argument.

    The implementation is based on Fred Glover et al: "Quantum Bridge Analytics I: A Tutorial on Formulating
    and Using QUBO Models", arXiv:1811.11538

    Args:
        graph (nx.Graph):
            A graph

    Returns:
            An instance of BinaryQuadraticModel with a QUBO formulation of the maximum cut
            problem for 'graph'.
    """
    linear: dict[int, int] = defaultdict(int)
    quadratic: dict[tuple[int, int], int] = defaultdict(int)
    for (i, j) in graph.edges:
        linear[i] += -1
        linear[j] += -1
        quadratic[(i, j)] = 2

    offset = 0.0
    vartype = dimod.BINARY
    return dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)


def maximum_cut(graph: nx.Graph) -> tuple[set[int], set[int], set[tuple[int, int]], set[tuple[int, int]]]:
    """Solves the maximum cut problem for the given graph, 'graph'. That is, the vertices
    of 'graph' is separated into two complementary subsets, s and s_c, such that the number
    of edges between s and s_c is as large as possible

    Args:
        graph (nx.Graph):
            A graph

    Returns:
            A tuple containing two complementary subsets of nodes, s and s_c, representing the
            maximum cut for the graph 'graph', along with two complementary sets of edges, comprising
            the sets of cut and uncut edges respectively.
    """
    bqm = generate_maximum_cut_bqm(graph)
    sample_label = "Maximum cut (" + str(graph.number_of_nodes()) + " nodes, " + str(graph.number_of_edges()) + " edges)"
    maximum_cut_info = sampler.sample_dwave(bqm, sample_label)
    assert (graph.number_of_nodes() == len(maximum_cut_info)), "Something went wrong... the maximum cut info doesn't match the input graph."
    
    nodes_set1: set[int] = set()
    nodes_set2: set[int] = set()
    for node in graph.nodes:
        if (maximum_cut_info[node]):
            nodes_set1.add(node)
        else:
            nodes_set2.add(node)

    cut_edges: set[tuple[int, int]] = set()
    uncut_edges: set[tuple[int, int]] = set()
    for (i, j) in graph.edges:
        if maximum_cut_info[i] != maximum_cut_info[j]:
            cut_edges.add((i, j))
        else:
            uncut_edges.add((i, j))

    return nodes_set1, nodes_set2, cut_edges, uncut_edges
