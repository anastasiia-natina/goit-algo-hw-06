def bfs_path(graph, start, end):
    queue = [start]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node == end:
            path = [current_node]
            while path[-1] != start:
                path.append(list(graph.predecessors(path[-1]))[0])
            path.reverse()
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)

    return None 