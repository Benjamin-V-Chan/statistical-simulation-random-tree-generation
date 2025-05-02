# Script to run many simulations and store results

# Imports
# - pandas
# - call generate_uniform_random_tree and generate_preferential_attachment_tree
# - call analyze_tree

# Define function run_simulations(num_simulations, n, model_type, output_filename):
#   Loop num_simulations times:
#       Generate a tree based on model_type ('uniform' or 'preferential')
#       Analyze the tree
#       Store results
#   Save all results into a CSV in outputs/ folder
