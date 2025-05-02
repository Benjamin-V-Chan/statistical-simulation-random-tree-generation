
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

