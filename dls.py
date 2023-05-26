def dls(root,goal,graph,visited,path,limit):
    if limit > 0:
        if root in visited:
            return
        visited.append(root)
        if root == goal:
            path.append(goal)
            return path
        for i in graph.get(root,[]):
                if dls(i,goal,graph,visited,path,limit-1):
                    path.insert(0,root)
                    return path

        return path


