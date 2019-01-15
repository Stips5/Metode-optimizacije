# -*- coding: utf-8 -*-
from collections import deque

def iterative_bfs(graph, end):
    q = deque([["Kevin Bacon"]])

    while q:
        path = q.popleft()

        v = path[-1]
        if v == end:
            return path, len(path)-1

        childrens = []
        for i in graph[v]:
            childrens.append(i)

        for child in childrens:
            nwPath = list(path)
            nwPath.append(child)
            q.append(nwPath)

    return None, -1
