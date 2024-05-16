def dfs_path(graph, start, end):
    stack = [(start, [])]

    while stack:
        current_node, path = stack.pop()
        visited = set(path)

        if current_node == end:
            return path + [current_node]

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                stack.append((neighbor, path + [current_node]))

    return None 