import argparse
import csv
import os
import collections
from collections import deque
from scripts._01_generate_random_tree import generate_random_tree  # adjust import path

def compute_metrics(adj):
    n = len(adj)
    def bfs(start):
        dist = {start:0}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    d1 = bfs(1)
    height = max(d1.values())
    far = max(d1, key=d1.get)
    d2 = bfs(far)
    diameter = max(d2.values())
    avg_branch = sum(len(adj[u]) - 1 for u in adj) / n
    return {"n": n, "height": height, "diameter": diameter, "avg_branch": avg_branch}

def run_for(n, reps):
    for _ in range(reps):
        adj = generate_random_tree(n)
        yield compute_metrics(adj)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ns", nargs="+", type=int, default=[50,100,200], help="list of node counts")
    p.add_argument("--reps", type=int, default=1000, help="trials per n")
    p.add_argument("--out", default="outputs/metrics.csv")
    args = p.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n","height","diameter","avg_branch"])
        for n in args.ns:
            for metrics in run_for(n, args.reps):
                w.writerow([metrics["n"], metrics["height"], metrics["diameter"], metrics["avg_branch"]])

if __name__ == "__main__":
    main()
