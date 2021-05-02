from __future__ import annotations
import networkx as nx


def is_vertex_cover(graph: nx.Graph, vertex_cover: vertex_cover) -> bool:
    """Determines whether the given set of vertices, 'vertex_cover', is a vertex
    cover of graph 'graph'.

    Given an undirected graph with a vertex set V and edge set E, a vertex cover
    is a subset of the vertices (nodes), V, such that each edge in E is incident
    to at least one node in the subset. I.e. all edges in E has at least one
    endpoint in the cover.

    Args:
        graph (nx.Graph):
            A graph
        vertex_cover (vertex_cover):
            A set of nodes, allegedly a vertex cover of 'graph'

    Returns:
            'true' if the set of nodes in 'vertex_cover' indeed is a vertex
            cover of 'graph'. Otherwise 'false' is returned.
    """

    return all(u in vertex_cover or v in vertex_cover for (u, v) in graph.edges)
