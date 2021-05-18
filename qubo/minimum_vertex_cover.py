from __future__ import annotations
from collections import defaultdict
import dimod
import math
import networkx as nx
import qubo.sampler as sampler


def generate_minimum_vertex_cover_bqm(graph: nx.Graph) -> dimod.BinaryQuadraticModel:
    """Generates an instance of BinaryQuadraticModel with a QUBO formulation of the
    minimum vertex cover for the graph given as argument.

    The implementation is based on Fred Glover et al: "Quantum Bridge Analytics I:
    A Tutorial on Formulating and Using QUBO Models", arXiv:1811.11538

    Args:
        graph (nx.Graph):
            A graph

    Returns:
            An instance of BinaryQuadraticModel with a QUBO formulation of the
            minimum vertex cover problem for 'graph'.
    """
    linear: dict[int, int] = defaultdict(int)
    quadratic: dict[tuple[int, int], int] = defaultdict(int)
    penalty = math.ceil(1.5 * graph.number_of_nodes())
    for (i, j) in graph.edges:
        linear[i] += -penalty
        linear[j] += -penalty
        quadratic[(i, j)] = penalty
    for i in graph.nodes:
        linear[i] += 1

    offset = 0.0
    vartype = dimod.BINARY
    return dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)


def minimum_vertex_cover(graph: nx.Graph) -> set[int]:
    """Generates a minimum vertex cover problem for the given graph, 'graph'. That is, a minimum
    subset of the nodes in 'graph' such that all edges in 'graph' has at least one endpoint in
    the subset.

    Args:
        graph (nx.Graph):
            A graph

    Returns:
            A set of nodes constituting the minimum vertex cover.
    """
    bqm = generate_minimum_vertex_cover_bqm(graph)
    sample_label = "Minimum vertex cover (" + str(graph.number_of_nodes()) + " nodes, " + str(graph.number_of_edges()) + " edges)"
    minimum_vertex_cover_info = sampler.sample_dwave(bqm, sample_label)
    assert (graph.number_of_nodes() == len(minimum_vertex_cover_info)), "Something went wrong... the minimum vertex cover info doesn't match the input graph."

    minimum_vertex_cover: set[int] = set()
    for node in graph.nodes:
        if (minimum_vertex_cover_info[node]):
            minimum_vertex_cover.add(node)
    assert (is_vertex_cover(graph, minimum_vertex_cover)), "The subset of nodes does not constitute a cover"

    return minimum_vertex_cover


def is_vertex_cover(graph: nx.Graph, vertex_cover: set[int]) -> bool:
    """Determines whether the given set of vertices, 'vertex_cover', is a vertex
    cover of graph 'graph'.

    Given an undirected graph with a vertex set V and edge set E, a vertex cover
    is a subset of the vertices (nodes), V, such that each edge in E is incident
    to at least one node in the subset. I.e. all edges in E has at least one
    endpoint in the cover.

    Args:
        graph (nx.Graph):
            A graph
        vertex_cover (set[int]):
            A set of nodes, allegedly a vertex cover of 'graph'

    Returns:
            'true' if the set of nodes in 'vertex_cover' indeed is a vertex
            cover of 'graph'. Otherwise 'false' is returned.
    """

    return all(u in vertex_cover or v in vertex_cover for (u, v) in graph.edges)
