import networkx as nx
import qubo.maximum_cut as mc

# Build a "seed graph", used as a base for our large example
seed_graph = nx.Graph()
seed_graph.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)])

# Build a graph by repeating the structure if the seed graph 'n' times. The sub graphs are
# connected with edges that are intended to be part of the maximum cut.
n = 20
graph = nx.Graph()
for i in range(n):
    if (i == 0):
        graph.add_edges_from(seed_graph.edges)
    else:
        for (u, v) in seed_graph.edges:
            graph.add_edge(u + i * 10, v + i * 10)
        # Connect with the previous graph (new edges should be part of the cut)
        graph.add_edge(3 + (i - 1) * 10, 1 + i * 10)
        graph.add_edge(4 + (i - 1) * 10, 0 + i * 10)

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
