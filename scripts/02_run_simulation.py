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

