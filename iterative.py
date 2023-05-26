def iterative(graph,goal,limit):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [(root,1)], [], [], []
    parent = {root: None}
    while stack:
        v,d = stack.pop()
        visited.append(v)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break

        for i in graph.get(v,[]):
            if i not in visited and d < limit:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append((temp.pop(),d+1))
    return path,visited







