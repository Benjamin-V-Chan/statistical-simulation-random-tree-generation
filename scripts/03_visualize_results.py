# 1. Parse parameters: path to stats CSV, output figures directory.
# 2. Load CSV into pandas DataFrame.
# 3. For each metric column (height, diameter, avg_degree, avg_path_length):
#      a. Plot a histogram.
#      b. Label axes and title.
#      c. Save figure to PNG in outputs/figures/.