def has_path(graph, src, dst):
    if graph is None:  #
        return False  # no need this two line
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    return False


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

print(has_path(graph, "f", "k"))
