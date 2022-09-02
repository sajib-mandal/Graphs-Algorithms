def depth_first_print(graph, start):
    stack = [start]
    while len(stack) > 0:
        current = stack[-1]    # -1 mean last element onn the list
        print(current)
        stack.pop()

        for neighbor in graph[current]:
            stack.append(neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

depth_first_print(graph, "a")

# output: [a, c, e, b, d, f]
