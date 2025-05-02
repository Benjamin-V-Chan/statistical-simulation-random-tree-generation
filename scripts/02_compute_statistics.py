import argparse
import json
import csv
import networkx as nx
import os

def compute_metrics(tree):
    G = nx.Graph()
    G.add_edges_from(tree["edges"])
    n = tree["n_nodes"]
    # height from node 1
    lengths = nx.single_source_shortest_path_length(G, 1)
    height = max(lengths.values())
    diameter = nx.diameter(G)
    avg_degree = sum(dict(G.degree()).values()) / n
    avg_path_length = nx.average_shortest_path_length(G)
    return {
        "tree_id": tree["tree_id"],
        "n_nodes": n,
        "height": height,
        "diameter": diameter,
        "avg_degree": round(avg_degree, 4),
        "avg_path_length": round(avg_path_length, 4)
    }

