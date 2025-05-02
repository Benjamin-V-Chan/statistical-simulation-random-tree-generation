# Script to generate random trees using different models

# Imports
# - random for random number generation
# - networkx for graph handling (allowed external library)
# - numpy for arrays and numerical operations

# Define function generate_uniform_random_tree(n):
#   Create a random spanning tree with n nodes
#   Use random edges with cycle removal (or use a Prüfer sequence method)
#   Return the tree (as a networkx graph)

# Define function generate_preferential_attachment_tree(n):
#   Create a tree by preferential attachment
#   Start with a single node
#   Iteratively add nodes
#     Each new node connects to an existing node with probability proportional to degree
#   Return the tree (as a networkx graph)
