import networkx as nx
import maximum_cut as mc

G = nx.Graph()
G.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])
nodes_set1, nodes_set2, cut_edges, uncut_edges = mc.maximum_cut(G)

print("Nodes in input graph: ", end="")
print(G.nodes)
print("Edges in input graph: ", end="")
print(G.edges)
print("Maximum cut node set 1: ", end="")
print(nodes_set1)
print("Maximum cut node set 2: ", end="")
print(nodes_set2)
print("Cut edges: ", end="")
print(cut_edges)
print("Uncut edges: ", end="")
print(uncut_edges)