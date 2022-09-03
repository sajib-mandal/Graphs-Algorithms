from collections import deque
def undirected_path(edges, node_A, node_B):
    # create helper function to convert "edges_list --> adjacency_list
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())  # set gives me O(1) lookup and O(1) insertion


def has_path(graph, src, dst, visited):
    queue = deque([src])

    while queue:
        current = queue[0]
        node = queue.popleft()
        if node == dst:
            return True
        if node in visited:
            return False
        queue.append(node)

        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def build_graph(edges):
    graph = {}  # graph using dict
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ("i", "j"),
    ("k", "i"),
    ("m", "k"),
    ("k", "l"),
    ("o", "n")
]

print(undirected_path(edges, "j", "m"))
