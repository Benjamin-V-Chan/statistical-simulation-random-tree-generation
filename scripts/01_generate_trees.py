import argparse
import random
import json
import os

def prufer_to_tree(prufer):
    m = len(prufer) + 2
    degree = [1] * (m)
    for p in prufer:
        degree[p - 1] += 1
    leaves = [i + 1 for i, d in enumerate(degree) if d == 1]
    leaves.sort()
    edges = []
    for p in prufer:
        leaf = leaves.pop(0)
        edges.append([leaf, p])
        degree[leaf - 1] -= 1
        degree[p - 1] -= 1
        if degree[p - 1] == 1:
            leaves.append(p)
            leaves.sort()
    edges.append(leaves)
    return edges

def generate_trees(n, m):
    trees = []
    for i in range(1, m + 1):
        prufer = [random.randint(1, n) for _ in range(n - 2)]
        edges = prufer_to_tree(prufer)
        trees.append({"tree_id": i, "n_nodes": n, "edges": edges})
    return trees

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nodes", type=int, default=50)
    p.add_argument("--count", type=int, default=1000)
    p.add_argument("--out", type=str, default="outputs/raw_trees.json")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    trees = generate_trees(args.nodes, args.count)
    with open(args.out, "w") as f:
        json.dump(trees, f, indent=2)

if __name__ == "__main__":
    main()
