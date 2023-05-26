def bfs(graph,goal):
    root = list(graph.keys())[0]
    queue, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while queue:
        v = queue.pop(0)
        if v in visited:
            continue
        visited.append(v)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        for i in graph.get(v,[]):
                 queue.append(i)
                 parent[i] = v
    return path,visited


