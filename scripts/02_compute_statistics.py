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

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", type=str, default="outputs/raw_trees.json")
    p.add_argument("--out", type=str, default="outputs/tree_stats.csv")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.inp) as f:
        trees = json.load(f)

    rows = [compute_metrics(t) for t in trees]
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
