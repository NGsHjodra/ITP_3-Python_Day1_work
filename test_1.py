def test_mst(): 
    # import the necessary packages
    import networkx as nx
    import matplotlib.pyplot as plt

    # create a weighted graph

    G = nx.Graph()

    # add nodes

    G.add_nodes_from([1,2,3,4,5])

    # add edges with random weights

    G.add_weighted_edges_from([(1,2,0.5),(1,3,0.75),(2,4,2),(3,4,5),(3,5,0.5),(4,5,0.75)])

    # create a minimum spanning tree

    T = nx.minimum_spanning_tree(G)

    # assert that the minimum spanning tree is a tree
    assert nx.is_tree(T)

    # assert that the minimum spanning tree has the correct edges
    assert [e for e in T.edges()] == [(1, 2), (1, 3), (3, 5), (4, 5)]