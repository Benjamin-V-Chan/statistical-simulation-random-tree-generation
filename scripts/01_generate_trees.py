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

