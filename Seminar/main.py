""" created by stips on 14.01.19. using PyCharm , python_version = 3.5 """
from collections import deque
from operator import attrgetter
import random
from Seminar.Edge import *

"""
Spanning        
    https://community.topcoder.com/stat?c=problem_statement&pm=3099
"""

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

def pathPrint(path):
    print("Graph edges")
    for i in path:
        print(i.node1, i.node2)
    print()

def isCircle(graph):
    if graph.__len__() == 0:
        return False

    start, _ = random.choice(list(graph.items()))
    queue = [start]
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

def iterative_bfs(graph):
    '''iterative breadth first search from start'''

    start, _ = random.choice(list(graph.items()))
    visited = []
    q = deque(start)
    while q:
        v = q.popleft()
        if v not in visited:
            visited.append(v)
        q.extend(w for w in graph[v] if w not in q and w not in visited)

    return visited

def isMST(graph, numNodes):
    if graph.__len__() < 1:
        return False

    path = iterative_bfs(makeListSusjedstva(graph))

    if path.__len__() == numNodes:
        return True
    else:
        return False

def kruskal(data, numOfNode, threshold):

    listOfEdgeObjects = readData(data)
    novaListaEdgeObjekata = list()

    listOfEdgeObjects.sort(key=attrgetter('length'))
    listOfEdgeObjects.sort(key=attrgetter('cost'))

    for edge in listOfEdgeObjects:
        if isMST(novaListaEdgeObjekata, numOfNode): break
        novaListaEdgeObjekata.append(edge)

        if isCircle(makeListSusjedstva(novaListaEdgeObjekata)):
            novaListaEdgeObjekata.pop()

        if novaListaEdgeObjekata.__len__() > 1:
            previous = novaListaEdgeObjekata[-2]
            last = novaListaEdgeObjekata[-1]
            if previous.node1 == last.node1 \
                    or previous.node1 == last.node2 \
                    or previous.node2 == last.node1 \
                    or previous.node2 == last.node2:
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
    graf, cost = kruskal(["0 1 4 1", "0 2 3 2", "1 2 1 4"], 3, 5)
    pathPrint(graf)
    if cost == 5:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 5 not ", cost)

    print()
    print("test sample ",  "\n","2 3 7 1", "\n", "3 1 9 1", "\n", "1 0 8 1", "\n", "3 0 1 5",  "\n","1 2 5 7",  "\n","0 2 8 4")
    graf, cost = kruskal(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 1000)
    pathPrint(graf)
    if cost == 3:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 3 not ", cost)

    print()
    print("test sample", "\n", "2 3 7 1",  "\n","3 1 9 1",  "\n","1 0 8 1",  "\n","3 0 1 5", "\n", "1 2 5 7",  "\n","0 2 8 4")
    graf, cost = kruskal(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 10)
    pathPrint(graf)
    if cost == 14:
        print("Ok")
        cnt += 1
    else:
        print("Error, expected result is 14 not ", cost)

    print()
    print("test sample", "0 1 5 5")
    graf, cost = kruskal(["0 1 5 5"], 2, 100)
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
    print("test sample", "\n", "2 3 7 1", "\n", "3 1 9 1", "\n", "1 0 8 1", "\n", "3 0 1 5", "\n", "1 2 5 7", "\n", "0 2 8 4")
    graf, cost = kruskal(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 10)
    pathPrint(graf)
    if cost == 14:
        print("Ok")
    else:
        print("Error, expected result is 14 not ", cost)

if __name__ == '__main__':
    # debug()
    test1()

