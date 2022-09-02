# breadth first traversel using queue

from collections import deque

def breath_first_print(graph, start):
    queue = deque([start])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

breath_first_print(graph, "a")

# output: [a, b, c, d, e, f]
