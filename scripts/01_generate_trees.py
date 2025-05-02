# 1. Parse parameters: number of nodes (n), number of trees (m), output path.
# 2. For each simulation i in 1..m:
#      a. Generate a random Prufer sequence of length n-2 with values 1..n.
#      b. Decode the Prufer sequence into an edge list representing a labeled tree.
#      c. Store edges (e.g., list of [u,v]) in a dict keyed by tree ID.
# 3. After all trees generated, write the list of tree-dicts to a JSON file.