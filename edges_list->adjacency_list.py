def undirected_path(edges, node_A, node_B):

    # create helper function to convert "edges_list --> adjacency_list
    graph = build_graph(edges)
    print(graph)


def build_graph(edges):
    graph = {}   # graph using dict
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
