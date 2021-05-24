import networkx as nx
import qubo.maximum_independent_vertex_set as mivs
import plot

graph = nx.wheel_graph(8)
maximum_independent_vertex_set = mivs.maximum_independent_vertex_set(graph)
print("Maximum independent vertex set: ", end="")
print(maximum_independent_vertex_set)

filename = "plots/maximum_independent_vertex_set.png"
plot.graph_with_colored_node_subset(graph, maximum_independent_vertex_set, filename)
print("\nYour plot is saved to '{}'".format(filename))
