from __future__ import annotations
import networkx as nx
import qubo.minimum_vertex_cover as mvc


def maximum_independent_vertex_set(graph: nx.Graph) -> set[int]:
    """Returns a maximum independent vertex set for the given graph.

    The definition from https://mathworld.wolfram.com/MaximumIndependentVertexSet.html reads:
    'An independent vertex set of a graph G is a subset of the vertices
    such that no two vertices in the subset represent an edge of G.
    Given a vertex cover of a graph, all vertices not in the cover
    define a independent vertex set. A maximum independent vertex
    set is an independent vertex set containing the largest possible
    number of vertices for a given graph

    Maximum independent vertex sets correspond to the complements of minimum vertex covers.'

    Consequently we find the maximum independent vertex set by finding
    the minimum vertex cover and taking the complement.

    Args:
        graph (nx.Graph):
            A graph

    Returns:
            A maximum independent vertex set for the input graph
    """
    minimum_vertex_cover = mvc.minimum_vertex_cover(graph)
    maximum_independent_vertex_set = {v for v in graph.nodes if v not in minimum_vertex_cover}
    assert (is_independent_vertex_set(graph, maximum_independent_vertex_set)), "The subset of nodes does not constitute an independent set"

    return {v for v in graph.nodes if v not in minimum_vertex_cover}


def is_independent_vertex_set(graph: nx.Graph, vertex_set: set[int]) -> bool:
    """Determines whether the given nodes form an independent set.

    An independent vertex set of a graph G is a subset of the vertices
    such that no two vertices in the subset represent an edge of G.
    I.e. the subgraph of G - induced by the nodes in the independent
    vertex set - contains no edges.

    Args:
        graph (nx.Graph):
            A graph
        vertex_set (set[int]):
            A subset of the vertices of 'graph'

    Returns:
            True if 'vertex_set' is an independent set of the vertices
            of 'graph'. Otherwise False
    """
    return len(graph.subgraph(vertex_set).edges) == 0
