import networkx as nx
import qubo.minimum_vertex_cover as mvc

seed_graph = nx.Graph()
seed_graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])

# Build a graph by repeating the structure if the seed graph 'n' times. The sub graphs are
# then connected with edges.
n = 20
graph = nx.Graph()
for i in range(n):
    if (i == 0):
        graph.add_edges_from(seed_graph.edges)
    else:
        for (u, v) in seed_graph.edges:
            graph.add_edge(u + i * 10, v + i * 10)
        # Connect with the previous graph
        graph.add_edge(3 + (i - 1) * 10, 1 + i * 10)
        graph.add_edge(4 + (i - 1) * 10, 1 + i * 10)
        graph.add_edge(0, i * 10)


minimum_vertex_cover = mvc.minimum_vertex_cover(graph)
print("Minimum vertex cover: ", end="")
print(minimum_vertex_cover)
