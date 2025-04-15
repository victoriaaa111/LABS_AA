import random
from generate_graphs import *

# convert unweighted graph to weighted graph
def convert_to_weighted(adj, min_weight=1, max_weight=10):
    n = len(adj)
    weighted_adj = [{} for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            if v not in weighted_adj[u]:
                weight = random.randint(min_weight, max_weight)
                weighted_adj[u][v] = weight
                weighted_adj[v][u] = weight
    return weighted_adj


# Kruskal's algorithm
def kruskal(adj):
    n = len(adj)
    parent = list(range(n))

    def find(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            return True
        return False

    edges = []
    for u in range(n):
        for v, w in adj[u].items():
            if u < v:
                edges.append((w, u, v))

    edges.sort()
    mst_weight = 0
    for w, u, v in edges:
        if union(u, v):
            mst_weight += w
    return mst_weight

# Prim's algorithm
def prim(adj):
    n = len(adj)
    selected = [False] * n
    selected[0] = True
    mst_weight = 0

    for _ in range(n - 1):
        min_edge = float('inf')
        u, v = -1, -1
        for i in range(n):
            if selected[i]:
                for j, w in adj[i].items():
                    if not selected[j] and w < min_edge:
                        min_edge = w
                        u, v = i, j
        if v != -1:
            selected[v] = True
            mst_weight += min_edge
    return mst_weight