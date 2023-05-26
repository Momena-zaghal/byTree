
def CostPath(path):
    Gn=0
    for (i , cost) in path:
        Gn+=cost
    return Gn + heuristic[path[-1][0]]
def AStarSearch(start,goal):
    graph = {
        1: {4: 2, 5: 1},
        4: {9: 5, 3: 1},
        5: {7: 3, 8: 4},
        9: {},
        3: {}, 7: {}, 8: {}}
    if start not in list(graph.keys()):
        return False
    queue=[[(start,0)]]
    visited=[]
    while queue:
        path=queue.pop(0)
        print(path)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            Child=graph.get(node,[])
            for i in Child:
                pathnode=path + [(i,Child[i])]
                queue.append(pathnode)
        queue.sort(key=CostPath)



heuristic={
    1:34,
    4:19,
    5:14,
    9:18,
    3:7,
    7:0,
    8:1
}
