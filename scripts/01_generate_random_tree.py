import random
import networkx as nx
import numpy as np

def generate_uniform_random_tree(n):
    prufer_sequence = [random.randint(0, n-1) for _ in range(n-2)]
    degree = [1] * n
    for node in prufer_sequence:
        degree[node] += 1
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for node in prufer_sequence:
        for i in range(n):
            if degree[i] == 1:
                G.add_edge(node, i)
                degree[node] -= 1
                degree[i] -= 1
                break
    u, v = [i for i in range(n) if degree[i] == 1]
    G.add_edge(u, v)
    return G

def generate_preferential_attachment_tree(n):
    G = nx.Graph()
    G.add_node(0)
    for i in range(1, n):
        degrees = np.array([G.degree(j) for j in G.nodes()])
        probs = degrees / degrees.sum()
        chosen_node = np.random.choice(list(G.nodes()), p=probs)
        G.add_edge(i, chosen_node)
    return G
