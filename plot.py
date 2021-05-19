from matplotlib import pyplot as plt
import networkx as nx
import matplotlib
matplotlib.use("agg")


def maximum_cut(graph, nodes_set1, nodes_set2, cut_edges, uncut_edges, filename):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, nodelist=nodes_set1, node_color='r')
    nx.draw_networkx_nodes(graph, pos, nodelist=nodes_set2, node_color='c')
    nx.draw_networkx_edges(graph, pos, edgelist=cut_edges, style='dashdot', alpha=0.5, width=3)
    nx.draw_networkx_edges(graph, pos, edgelist=uncut_edges, style='solid', width=3)
    nx.draw_networkx_labels(graph, pos)

    plt.savefig(filename, bbox_inches='tight')


def minimum_vertex_cover(graph, minimum_vertex_cover, filename):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, nodelist=graph.nodes, node_color='r')
    nx.draw_networkx_nodes(graph, pos, nodelist=minimum_vertex_cover, node_color='c')
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, style='solid', width=3)
    nx.draw_networkx_labels(graph, pos)

    plt.savefig(filename, bbox_inches='tight')
