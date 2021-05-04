import networkx as nx
import qubo.maximum_cut as mc
import plot

graph = nx.Graph()
graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])
nodes_set1, nodes_set2, cut_edges, uncut_edges = mc.maximum_cut(graph)

print("Nodes in input graph: ", end="")
print(graph.nodes)
print("Edges in input graph: ", end="")
print(graph.edges)
print("Maximum cut node set 1: ", end="")
print(nodes_set1)
print("Maximum cut node set 2: ", end="")
print(nodes_set2)
print("Cut edges: ", end="")
print(cut_edges)
print("Uncut edges: ", end="")
print(uncut_edges)

filename = "plots/maxcut_plot.png"
plot.maximum_cut(graph, nodes_set1, nodes_set2, cut_edges, uncut_edges, filename)
print("\nYour plot is saved to '{}'".format(filename))
