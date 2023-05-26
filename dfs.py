def dfs(graph,goal):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while stack:
        v = stack.pop()
        visited.append(v)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        for i in graph.get(v,[]):
            if i not in visited:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append(temp.pop())
    return path,visited




