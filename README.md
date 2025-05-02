# statistical-simulation-random-tree-generation

## Project Overview

This project simulates **random labeled trees** and performs statistical analysis on structural properties such as height, diameter, average degree, and average shortest-path length. The generation process is based on **Prufer sequences**, a combinatorial encoding method that uniquely maps sequences to trees.

### Mathematical Foundation

**1. Prufer Sequence Representation:**

Each labeled tree with \$n\$ nodes corresponds to a unique Prufer sequence of length \$(n-2)\$, where each element is an integer from \$1\$ to \$n\$. Thus, there are:

$$
n^{n-2}
$$

total distinct labeled trees, as stated by **Cayley's formula**.

**Proof Outline for Cayley's Formula:**

* For \$n\$ labeled vertices, a Prufer sequence of length \$(n-2)\$ can be generated where each entry is any of the \$n\$ vertices.
* Each sequence corresponds bijectively to a unique tree.
* Hence, the total number of trees is \$n^{n-2}\$.

**2. Tree Properties:**

* **Height (\$h\$):**
  The height of a tree rooted at node \$1\$ is the maximum distance from the root to any other node. Using BFS (Breadth-First Search), the height is:

$$
h = \max_{v \in V} d(1, v)
$$

where \$d(1, v)\$ is the shortest-path distance.

* **Diameter (\$D\$):**
  The longest shortest-path between any two nodes in the tree:

$$
D = \max_{u, v \in V} d(u, v)
$$

* **Average Degree (\$\bar{d}\$):**
  Since a tree with \$n\$ nodes has exactly \$n-1\$ edges, the average degree is:

$$
\bar{d} = \frac{2(n-1)}{n}
$$

* **Average Shortest-Path Length (ASPL):**

$$
ASPL = \frac{1}{\binom{n}{2}} \sum_{\substack{u, v \in V \\ u < v}} d(u,v)
$$

where \$\binom{n}{2}\$ is the number of node pairs.

This project statistically analyzes how these quantities behave across thousands of random trees, revealing probabilistic behaviors of random structures.

---

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
