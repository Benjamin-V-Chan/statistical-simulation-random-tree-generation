# statistical-simulation-random-tree-generation

## Project Overview

This project simulates **random labeled trees** and performs statistical analysis on structural properties such as height, diameter, average degree, and average shortest-path length. The generation process is based on **Prufer sequences**, a combinatorial encoding method that uniquely maps sequences to trees.

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_trees.py
│   ├── 02_compute_statistics.py
│   └── 03_visualize_results.py
├── outputs/
│   ├── raw_trees.json
│   ├── tree_stats.csv
│   └── figures/
│       ├── height_hist.png
│       ├── diameter_hist.png
│       ├── avg_degree_hist.png
│       └── avg_path_length_hist.png
├── requirements.txt
└── README.md
```
