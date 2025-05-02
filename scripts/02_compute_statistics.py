# 1. Parse parameters: path to raw trees JSON, output CSV path.
# 2. Load JSON, iterate over each tree:
#      a. Build a graph (e.g., with networkx) from its edge list.
#      b. Compute:
#           - n_nodes
#           - height (max distance from node 1 via BFS)
#           - diameter (longest shortest path in the tree)
#           - average degree
#           - average shortest-path length
#      c. Append metrics as a row in a list.
# 3. Write all rows to a CSV with headers.