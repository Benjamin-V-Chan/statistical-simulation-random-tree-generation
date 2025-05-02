# scripts/02_run_simulations.py

"""
PSEUDOCODE:

# 1. IMPORT argparse, csv, os, statistics, multiprocessing (optional), and
#    from 01_generate_random_tree import generate_random_tree
# 2. FUNCTION compute_metrics(adj):
#      - pick node 1 as root; do BFS to get height (max distance)
#      - do BFS twice to compute diameter: from arbitrary node,
#        find farthest node A; then BFS from A to farthest distance
#      - compute average branching factor: (sum(degree-1) / n)
#      - return dict: {"n":n, "height":h, "diameter":d, "avg_branch":b}
# 3. FUNCTION run_for(n, reps):
#      - for i in range(reps):
#           • adj = generate_random_tree(n)
#           • yield compute_metrics(adj)
# 4. FUNCTION main():
#      - parse args: ns (list of ints), reps (int), --out
#      - open CSV writer with headers
#      - for each n in ns: for each result in run_for(n, reps): write row
"""

