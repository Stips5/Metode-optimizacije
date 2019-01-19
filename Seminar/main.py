""" created by stips on 14.01.19. using PyCharm , python_version = 3.5 """
from collections import deque

from Seminar.Edge import *

"""
Spanning        
    https://community.topcoder.com/stat?c=problem_statement&pm=3099

Given a connected graph with nodes nodes, where each edge is undirected and has both a length and a cost, 
your task is to pick a subset of the edges such that the graph is still connected, 
the minimum distance between each pair of nodes is less than or equal to threshold, and the total cost is minimized. 
You should return this minimum cost. The graph will be given as a String[], g, each element of which represents an edge in the form "u v length cost", 
where u and v are the zero-based indices of the two nodes connected by this edge. For example, consider the following input:

nodes = 3
threshold = 5
g = {"0 1 4 1","0 2 3 2","1 2 1 4"}

If we select the first and second edges, then the distance between nodes 1 and 2 ends up being 7, greater than our threshold. 
However, if we pick the first and third edges, the distance between all pairs of nodes is 5 or less, 
and the cost is minimized (picking the second and third edges would cost more). Thus, we return the cost of these two edges, 5.

Constraints
-	g will contain between 1 and 18 elements, inclusive.
-	nodes will be between 2 and 10, inclusive.
-	threshold will be between 1 and 1000, inclusive.
-	Each element of g will be formatted as "u v length cost", where u, v, length and cost are all integers with no extra leading zeros.
-	Each u and v will be between 0 and nodes-1, inclusive.
-	Each length and cost will be between 1 and 100, inclusive.
-	No two elements of g will refer to edges between the same pair of nodes.
-	In each element of g, u will not equal v.
-	If you use all of the edges, the graph will be connected, and the minimum distance between each pair of nodes will be less than or equal to threshold.
"""

from operator import attrgetter

def getListOfNodes(listaEdgeObje):
    listaNodeova = list()

    for e in listaEdgeObje:
        n1, n2 = e.node1, e.node2

        if n1 not in listaNodeova:
            listaNodeova.append(n1)
        if n2 not in listaNodeova:
            listaNodeova.append(n2)

    return listaNodeova

def makeListSusjedstva(edgeObjectList):
    listaSusjedstva = dict()
    vrhovi = getListOfNodes(edgeObjectList)

    for i in vrhovi:
        listaSusjedstva[i] = []

    for e in edgeObjectList:
        n1, n2 = e.node1, e.node2

        if n2 not in listaSusjedstva[n1]:
            listaSusjedstva[n1].append(n2)
        if n1 not in listaSusjedstva[n2]:
            listaSusjedstva[n2].append(n1)

    return listaSusjedstva

def readData(input):
    listOfEdges = list()

    for line in input:
        l = line.split(" ")
        e = Edge(l[0], l[1], l[2], l[3])
        listOfEdges.append(e)

    return listOfEdges

def isCircle(graph, start_point):
    if graph.__len__() == 0:
        return False

    queue = [start_point]
    visited = set()
    visited.add(queue[0])
    while queue:
        from_point = queue.pop(0)
        for to_point in graph[from_point]:
            if to_point in visited:
                return True
            else:
                queue.append(to_point)
                visited.add(to_point)
            graph[to_point].remove(from_point)
    return False

def pathPrint(path):
    print("Graph edges")
    for i in path:
        print(i.node1, i.node2)
    print()

def iterative_bfs(graph, start):
    '''iterative breadth first search from start'''
    path = []
    q = deque(start)
    while q:
        v = q.popleft()
        if v not in path:
            path.append(v)
        q.extend(w for w in graph[v] if w not in q and w not in path)

    print(path)
    return path

def isOver(graph, numNodes):
    if graph.__len__() < 1:
        return False

    path = iterative_bfs(makeListSusjedstva(graph), graph[0].node1)

    if path.__len__() == numNodes:
        return True
    else:
        return False

def kruskov(data, numOfNode, threshold):

    listOfEdgeObjects = readData(data)
    novaListaEdgeObjekata = list()

    listOfEdgeObjects.sort(key=attrgetter('length'))  #sort by length
    listOfEdgeObjects.sort(key=attrgetter('cost'))  # sort by cost

    for edge in listOfEdgeObjects:
        if isOver(novaListaEdgeObjekata, numOfNode):     #broji visited i vidit jel odgovara broju nodeova
            break
        novaListaEdgeObjekata.append(edge)

        #provjeri je li napravilo krug
        if isCircle(makeListSusjedstva(novaListaEdgeObjekata), listOfEdgeObjects[0].node1):
            novaListaEdgeObjekata.pop()

        #dohvati zadnja dva elemeta i provjeri jel im length veci od thresholda
        if novaListaEdgeObjekata.__len__() > 1:
            previous = novaListaEdgeObjekata[-2]
            last = novaListaEdgeObjekata[-1]
            connectedLen = int(previous.length) + int(last.length)
            if connectedLen > threshold:
                novaListaEdgeObjekata.remove(last)

    sum = 0
    for e in novaListaEdgeObjekata:
        sum += int(e.cost)

    return novaListaEdgeObjekata, sum

def test1():
    cnt = 0

    print()
    print("test sample ", "\n", "0 1 4 1", "\n","0 2 3 2","\n","1 2 1 4")
    graf, cost = kruskov(["0 1 4 1","0 2 3 2","1 2 1 4"], 3, 5)
    pathPrint(graf)
    if cost == 5:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 5 not ", cost)

    print()
    print("test sample ",  "\n","2 3 7 1", "\n", "3 1 9 1", "\n", "1 0 8 1", "\n", "3 0 1 5",  "\n","1 2 5 7",  "\n","0 2 8 4")
    graf, cost = kruskov(["2 3 7 1","3 1 9 1","1 0 8 1","3 0 1 5","1 2 5 7","0 2 8 4"], 4, 1000)
    pathPrint(graf)
    if cost == 3:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 3 not ", cost)

    print()
    print("test sample", "\n", "2 3 7 1",  "\n","3 1 9 1",  "\n","1 0 8 1",  "\n","3 0 1 5", "\n", "1 2 5 7",  "\n","0 2 8 4")
    graf, cost = kruskov(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 10)
    pathPrint(graf)
    if cost == 14:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 14 not ", cost)

    print()
    print("test sample", "0 1 5 5")
    graf, cost = kruskov(["0 1 5 5"], 2, 100)
    pathPrint(graf)
    if cost == 5:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 5 not ", cost)



    print()
    print(cnt / 4, "%")

def debug():


    print()
    print("test sample ",  "\n","2 3 7 1", "\n", "3 1 9 1", "\n", "1 0 8 1", "\n", "3 0 1 5",  "\n","1 2 5 7",  "\n","0 2 8 4")
    graf, cost = kruskov(["2 3 7 1","3 1 9 1","1 0 8 1","3 0 1 5","1 2 5 7","0 2 8 4"], 4, 1000)
    pathPrint(graf)
    if cost == 3:
        print("Ok")
    else:
        print("Error, expected result is 3 not ", cost)

    # print()
    # print("test sample", "\n", "2 3 7 1", "\n", "3 1 9 1", "\n", "1 0 8 1", "\n", "3 0 1 5", "\n", "1 2 5 7", "\n", "0 2 8 4")
    # graf, cost = kruskov(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 10)
    # pathPrint(graf)
    # if cost == 14:
    #     print("Ok")
    # else:
    #     print("Error, expected result is 14 not ", cost)

if __name__ == '__main__':
    # debug()
    test1()

