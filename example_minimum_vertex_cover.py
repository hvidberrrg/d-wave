import networkx as nx
import qubo.minimum_vertex_cover as mvc

graph = nx.Graph()
graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])
minimum_vertex_cover = mvc.minimum_vertex_cover(graph)

print("Nodes in input graph: ", end="")
print(graph.nodes)
print("Minimum vertex cover: ", end="")
print(minimum_vertex_cover)
