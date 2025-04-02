import time
import random
import matplotlib.pyplot as plt
from collections import deque


# graph generation functions
# generate a complete graph with n nodes.
def generate_complete_graph(n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].append(j)
    return adj


# generate a dense graph with n nodes
def generate_dense_graph(n, edge_ratio=0.8):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < edge_ratio:
                adj[i].append(j)
    return adj


# generate a sparse graph with n nodes and approximately 2n edges
def generate_sparse_graph(n):
    adj = [[] for _ in range(n)]
    # create a spanning tree first to ensure connectivity
    for i in range(1, n):
        parent = random.randint(0, i - 1)
        adj[parent].append(i)
        adj[i].append(parent)

    # add a few more random edges to make it more than just a tree
    extra_edges = n // 2
    for _ in range(extra_edges):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    return adj


# generate a binary tree with n nodes.
def generate_tree_graph(n):
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        parent = (i - 1) // 2
        adj[parent].append(i)
        adj[i].append(parent)
    return adj


# generate a path graph with n nodes
def generate_path_graph(n):
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[i].append(i + 1)
        adj[i + 1].append(i)
    return adj


# generate a star graph with n nodes.
def generate_star_graph(n):
    adj = [[] for _ in range(n)]
    # node 0 is the center
    for i in range(1, n):
        adj[0].append(i)
        adj[i].append(0)
    return adj


# generate a disconnected graph with n nodes divided into components
def generate_disconnected_graph(n):
    adj = [[] for _ in range(n)]

    # create approximately sqrt(n) components
    num_components = max(2, int(n ** 0.5))
    nodes_per_component = n // num_components

    for c in range(num_components):
        start = c * nodes_per_component
        end = (c + 1) * nodes_per_component if c < num_components - 1 else n

        # create a small connected component
        for i in range(start + 1, end):
            parent = random.randint(start, i - 1)
            adj[parent].append(i)
            adj[i].append(parent)

    return adj


def bfs(adj):
    n = len(adj)
    visited = [False] * n
    result = []
    queue = deque([0])  # Start from node 0
    visited[0] = True

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                vertex = queue.popleft()
                result.append(vertex)

                for neighbor in adj[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return result


def dfs(adj):
    n = len(adj)
    visited = [False] * n
    result = []

    for start in range(n):
        if not visited[start]:
            stack = [start]

            while stack:
                vertex = stack.pop()
                if not visited[vertex]:
                    visited[vertex] = True
                    result.append(vertex)

                    for neighbor in reversed(adj[vertex]):
                        if not visited[neighbor]:
                            stack.append(neighbor)

    return result


# function to measure execution time
def measure_time(algorithm, graph):
    start_time = time.time()
    algorithm(graph)
    end_time = time.time()
    return (end_time - start_time) * 1000  # convert to milliseconds
