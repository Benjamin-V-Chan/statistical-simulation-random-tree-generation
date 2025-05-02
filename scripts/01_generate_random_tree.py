# scripts/01_generate_random_tree.py

"""
PSEUDOCODE:

# 1. IMPORT modules: random, csv, argparse, os
# 2. FUNCTION generate_prufer_sequence(n):
#      - RETURN a list of length n-2 with integers 1..n chosen uniformly at random
# 3. FUNCTION prufer_to_tree(prufer_seq):
#      - let m = len(prufer_seq)+2
#      - initialize degree[i] = 1 for i in 1..m
#      - for each k in prufer_seq: degree[k] += 1
#      - initialize empty edge list
#      - for each k in prufer_seq:
#           • find the smallest i with degree[i]==1
#           • add edge (i,k)
#           • decrement degree[i] and degree[k]
#      - two nodes with degree==1 remain; add edge between them
#      - return adjacency dict mapping each node to its list of neighbors
# 4. FUNCTION generate_random_tree(n):
#      - seq = generate_prufer_sequence(n)
#      - return prufer_to_tree(seq)
# 5. IF __name__ == "__main__":
#      - parse args: n (int), --out (path to save .csv)
#      - call generate_random_tree(n)
#      - write adjacency list: each row “node,neighbor1 neighbor2 …”
"""
