
import random
import csv
import argparse
import os

def generate_prufer_sequence(n):
    return [random.randint(1, n) for _ in range(n-2)]

def prufer_to_tree(prufer_seq):
    m = len(prufer_seq) + 2
    degree = {i:1 for i in range(1, m+1)}
    for k in prufer_seq:
        degree[k] += 1
    edges = []
    for k in prufer_seq:
        leaf = min(i for i,d in degree.items() if d==1)
        edges.append((leaf, k))
        degree[leaf] -= 1
        degree[k]   -= 1
    u, v = [i for i,d in degree.items() if d==1]
    edges.append((u, v))
    adj = {i:[] for i in range(1, m+1)}
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def generate_random_tree(n):
    seq = generate_prufer_sequence(n)
    return prufer_to_tree(seq)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("n", type=int, help="number of nodes")
    p.add_argument("--out", default="outputs/tree.csv", help="where to save adjacency")
    args = p.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    tree = generate_random_tree(args.n)
    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["node", "neighbors"])
        for node, nbrs in tree.items():
            w.writerow([node, " ".join(map(str,nbrs))])
