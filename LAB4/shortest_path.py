import time
import matplotlib.pyplot as plt
import random
from generate_graphs import (
    generate_complete_graph,
    generate_dense_graph,
    generate_sparse_graph,
    generate_tree_graph,
    generate_directed_graph,
    generate_undirected_graph,
    generate_cyclic_graph,
    generate_acyclic_graph,
    generate_weighted_graph,
    generate_grid_graph,
    generate_connected_graph,
    generate_disconnected_graph
)

def dijkstra(adj, start):
    n = len(adj)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    nodes_to_process = [start]

    while nodes_to_process:
        u = None
        min_dist = float('inf')
        for node in nodes_to_process:
            if dist[node] < min_dist and not visited[node]:
                min_dist = dist[node]
                u = node

        if u is None:
            break

        visited[u] = True
        nodes_to_process.remove(u)

        for v, weight in adj[u].items():
            if not visited[v]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    if v not in nodes_to_process:
                        nodes_to_process.append(v)
    return dist

def floyd_warshall(adj):
    n = len(adj)
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize distance matrix
    for i in range(n):
        dist[i][i] = 0
        for j, weight in adj[i].items():
            dist[i][j] = weight

    # Floyd-Warshall main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# function to add weights to an unweighted graph
def add_weights(adj):
    weighted_adj = [{} for _ in range(len(adj))]
    for u in range(len(adj)):
        for v in adj[u]:
            # assign random weights between 1 and 10
            weighted_adj[u][v] = random.randint(1, 10)
    return weighted_adj


# test functions for each algorithm
def test_dijkstra(adj):
    start_time = time.time()
    for i in range(len(adj)):
        dijkstra(adj, i)
    return time.time() - start_time


def test_floyd_warshall(adj):
    start_time = time.time()
    floyd_warshall(adj)
    return time.time() - start_time


# Generate weighted versions of all graph types
def generate_all_weighted_graphs(n):
    graphs = {
        "Complete": add_weights(generate_complete_graph(n)),
        "Dense": add_weights(generate_dense_graph(n)),
        "Sparse": add_weights(generate_sparse_graph(n)),
        "Tree": add_weights(generate_tree_graph(n)),
        "Directed": add_weights(generate_directed_graph(n)),
        "Undirected": add_weights(generate_undirected_graph(n)),
        "Cyclic": add_weights(generate_cyclic_graph(n)),
        "Acyclic": add_weights(generate_acyclic_graph(n)),
        "Weighted": generate_weighted_graph(n),  # already weighted
        "Grid": add_weights(generate_grid_graph(n)),
        "Connected": add_weights(generate_connected_graph(n)),
        "Disconnected": add_weights(generate_disconnected_graph(n))
    }
    return graphs


def plot_overall_results(sizes, results):
    plt.figure(figsize=(12, 8))

    # Dijkstra overall
    plt.subplot(2, 1, 1)
    for graph_type in results['Dijkstra']:
        # only plot if we have results for this graph type
        if len(results['Dijkstra'][graph_type]) == len(sizes):
            plt.plot(sizes, results['Dijkstra'][graph_type], label=graph_type, marker='o')
    plt.title('Dijkstra Algorithm Performance')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    # Floyd-Warshall overall
    plt.subplot(2, 1, 2)
    for graph_type in results['Floyd-Warshall']:
        #only plot if we have results for this graph type
        if len(results['Floyd-Warshall'][graph_type]) == len(sizes):
            plt.plot(sizes, results['Floyd-Warshall'][graph_type], label=graph_type, marker='o')
    plt.title('Floyd-Warshall Algorithm Performance')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_individual_graph_results(sizes, results):
    graph_types = list(results['Dijkstra'].keys())

    for graph_type in graph_types:
        plt.figure(figsize=(10, 6))
        has_data = False

        # only plot if we have data for this graph type
        if len(results['Dijkstra'].get(graph_type, [])) == len(sizes):
            plt.plot(sizes, results['Dijkstra'][graph_type], '-', marker='o', label='Dijkstra', color='violet')
            has_data = True

        if len(results['Floyd-Warshall'].get(graph_type, [])) == len(sizes):
            plt.plot(sizes, results['Floyd-Warshall'][graph_type], '-', marker='x', label='Floyd-Warshall',
                     color='slateblue')
            has_data = True

        if has_data:
            plt.title(f'Performance on {graph_type} Graph')
            plt.xlabel('Number of Nodes')
            plt.ylabel('Time (seconds)')
            plt.legend()
            plt.grid(True)
            plt.show()


def run_tests(max_nodes=500, step=10):
    sizes = list(range(1, max_nodes + 1, step))
    graph_types = [
        "Complete", "Dense", "Sparse", "Tree",
        "Directed", "Undirected", "Cyclic", "Acyclic",
        "Weighted", "Grid", "Connected", "Disconnected"
    ]

    results = {
        'Dijkstra': {gt: [] for gt in graph_types},
        'Floyd-Warshall': {gt: [] for gt in graph_types}
    }

    for size in sizes:
        print(f"Testing size: {size}")
        graphs = generate_all_weighted_graphs(size)

        for graph_type in graph_types:
            adj = graphs[graph_type]

            # test Dijkstra
            try:
                time_dijkstra = test_dijkstra(adj)
                results['Dijkstra'][graph_type].append(time_dijkstra)
            except Exception as e:
                print(f"Error with Dijkstra on {graph_type} graph (size {size}): {e}")
                results['Dijkstra'][graph_type].append(float('nan'))

            # Test Floyd-Warshall
            try:
                time_floyd = test_floyd_warshall(adj)
                results['Floyd-Warshall'][graph_type].append(time_floyd)
            except Exception as e:
                print(f"Error with Floyd-Warshall on {graph_type} graph (size {size}): {e}")
                results['Floyd-Warshall'][graph_type].append(float('nan'))

    return sizes, results

# Main execution
if __name__ == "__main__":
    sizes, results = run_tests(max_nodes=300, step=10)
    plot_overall_results(sizes, results)
    plot_individual_graph_results(sizes, results)