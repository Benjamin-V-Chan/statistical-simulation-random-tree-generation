import networkx as nx
import numpy as np

def analyze_tree(G):
    num_nodes = G.number_of_nodes()
    num_leaves = sum(1 for node in G.nodes() if G.degree(node) == 1)
    degrees = [G.degree(node) for node in G.nodes()]
    avg_degree = np.mean(degrees)
    max_degree = np.max(degrees)
    diameter = nx.diameter(G)
    avg_path_length = nx.average_shortest_path_length(G)
    
    return {
        'num_nodes': num_nodes,
        'num_leaves': num_leaves,
        'avg_degree': avg_degree,
        'max_degree': max_degree,
        'diameter': diameter,
        'avg_path_length': avg_path_length
    }
