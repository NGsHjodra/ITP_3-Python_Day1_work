# import the necessary packages
import networkx as nx
import matplotlib.pyplot as plt

# create a weighted graph

G = nx.Graph()

# add nodes

G.add_nodes_from([1,2,3,4,5])

# add edges with random weights

G.add_weighted_edges_from([(1,2,0.5),(1,3,0.75),(2,4,2),(3,4,5),(3,5,0.5),(4,5,0.75)])

# create a layout

pos = nx.spring_layout(G)

# draw the graph and edge labels

nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# save the graph as a png file

plt.savefig("weighted_graph.png")

# clear the plot

plt.clf()

# create a minimum spanning tree

T = nx.minimum_spanning_tree(G)

# draw the minimum spanning tree and edge labels with different colors

nx.draw(T, pos, with_labels=True, node_color='red', edge_color='red')
nx.draw_networkx_edge_labels(T, pos, edge_labels=nx.get_edge_attributes(T, 'weight'), font_color='red')

plt.show()
