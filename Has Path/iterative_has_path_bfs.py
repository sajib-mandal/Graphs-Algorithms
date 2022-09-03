from collections import deque


def has_path(graph, src, dst):

    queue = deque([src])

    while len(queue) >= 0:

        current = queue[0]
        node = queue.popleft()

        if node == dst:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)
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
