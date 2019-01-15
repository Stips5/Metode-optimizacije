""" created by stips on 14.01.19. using PyCharm , python_version = 3.5 """

from Seminar.Edge import Edge

#radi
def initMatricaUdaljenosti(n):
    matricaUdaljenosti = [[float('inf') for x in range(n)]for x in range(n)]

    for i in range(n):
        matricaUdaljenosti[i][i] = 0

    return matricaUdaljenosti

#radi
def putUdaljenostiUMatricuUdaljenosti(matricaUdaljenost, listaEdgeva):
    for e in listaEdgeva:
        n1, n2 = int(e.node1), int(e.node2)
        matricaUdaljenost[n1][n2], matricaUdaljenost[n2][n1] = e.length, e.length
    return matricaUdaljenost

#radi
def ispisMatriceUdaljenosti(numOfNodes, matricaUdaljenosti):
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            print(matricaUdaljenosti[i][j], end=" ")
        print()

def findCheapestPath(graph, numOfNodes, threshold):
    listaEdgeva = readData(graph)
    matricaUdaljenosti = initMatricaUdaljenosti(numOfNodes)

    for i in listaEdgeva:
        print(i)

        if int(i.length) > threshold:
            print(i, "removed, its grater than threshold")
            listaEdgeva.remove(i)

    print()
    listNodeova = getListOfNodes(listaEdgeva)
    print("Nodes")
    print(listNodeova)

    print()
    print("Lista susjedstva")
    listaSusjedstva = makeListSusjedstva(listNodeova, listaEdgeva)

    for k, v in listaSusjedstva.items():
        print(k, v)

    print()
    print("matrica udaljenosti")

    matricaUdaljenosti = putUdaljenostiUMatricuUdaljenosti(matricaUdaljenosti, listaEdgeva)
    ispisMatriceUdaljenosti(numOfNodes, matricaUdaljenosti)

#radi
def makeListSusjedstva(vrhovi, edgevi):
    listaSusjedstva = dict()

    for i in vrhovi:
        listaSusjedstva[i] = []

    for e in edgevi:
        n1, n2 = e.node1, e.node2

        if n2 not in listaSusjedstva[n1]:
            listaSusjedstva[n1].append(n2)
        if n1 not in listaSusjedstva[n2]:
            listaSusjedstva[n2].append(n1)


    return listaSusjedstva

def getListOfNodes(l):
    listaN = list()

    for i in l:
        if listaN.__contains__(i.node1):  pass
        else:   listaN.append(i.node1)

        if listaN.__contains__(i.node2):  pass
        else:   listaN.append(i.node2)

    return listaN

def readData(input):
    listOfEdges = list()

    for line in input:
        l = line.split(" ")
        e = Edge(l[0], l[1], l[2], l[3])
        listOfEdges.append(e)

    return listOfEdges

if __name__ == '__main__':

    # cost = findCheapestPath(["0 1 5 5"], 2, 100)
    # if cost == 5: print("Ok")
    # else:   print("Error, expected result is 5")

    cost = findCheapestPath(["0 1 4 1", "0 2 3 2", "1 2 1 4"], 3, 5)
    # if cost == 5: print("Ok")
    # else:   print("Error, expected result is 5")

    # cost = findCheapestPath(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 1000)
    # if cost == 3: print("Ok")
    # else:   print("Error, expected result is 3")

    # cost = findCheapestPath(["2 3 7 1", "3 1 9 1", "1 0 8 1", "3 0 1 5", "1 2 5 7", "0 2 8 4"], 4, 10)
    # if cost == 14: print("Ok")
    # else:   print("Error, expected result is 14")

    # cost = findCheapestPath(["6 8 19 19", "1 3 98 75", "6 7 60 91", "4 6 89 53", "2 7 84 100", "9 5 31 65", "8 7 51 80", "1 4 78 94", "9 3 68 43", "7 0 20 77", "4 7 89 20", "4 2 82 21", "8 0 30 36", "8 3 44 100", "1 8 41 56", "8 2 27 66", "7 5 50 3", "9 7 45 71"g, 10, 190)
    # if cost == 442: print("Ok")
    # else:   print("Error, expected result is 442")

    # cost = findCheapestPath(["0 1 1 100", "1 2 1 1", "2 3 1 1", "3 4 1 1", "4 5 1 1", "5 6 1 1", "6 7 1 1", "5 8 1 1", "5 9 1 1", "1 3 1 1","1 4 1 1", "3 9 1 1", "2 8 1 1", "2 5 1 1", "2 4 1 1", "7 9 1 1", "6 8 1 1", "6 9 1 1"],10,100)
    # if cost == 108: print("Ok")
    # else:   print("Error, expected result is 108")


