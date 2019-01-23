""" created by stips on 22.1.19. using PyCharm , python_version = 3.5 """
import random
from collections import deque

keywords = ("*vertices", "*arcs")

def read(fileName):
    file = open(fileName, "r")

    '''cita prvi red i gleda koliko ima tocaka pa svaku tocku ucita'''

    # arcs usmjereni , edge veza

    row = file.readline()
    while row != None:
        row = row.strip("\n")

        '''provjerava jel red u fileu sa headerima da zna di ce spremat'''

        if row.__contains__(keywords[0]):  # vrhovi
            n = row.replace(keywords[0], "").replace(" ", "")
            readVrhovi(file, int(n))
        row = readUsmjVeze(file)

    return vrhovi, usmjVeze

def readVrhovi(file, n):
    cnt = 0
    for row in file:
        if row.__contains__(keywords[1]):
            return
        cnt += 1
        splited = row.replace("\n", "").split('"')
        vrhovi[splited[1]] = int(splited[0])
        if cnt == n:
            break

def readUsmjVeze(file):
    for row in file:
        kae = [int(s) for s in row.split() if s.isdigit()]

        if kae[0] in vrhovi.values() and kae[1] in vrhovi.values():
            usmjVeze.append([kae[0], kae[1]])

def convertToListaSusjedstva(usmjVeze):
    listaSusjedstva = dict()

    for k, v in vrhovi.items():
        listaSusjedstva[v] = []

    for e in usmjVeze:
        n1, n2 = e

        try:
            if n2 not in listaSusjedstva[n1]:
                listaSusjedstva[n1].append(n2)
            if n1 not in listaSusjedstva[n2]:
                listaSusjedstva[n2].append(n1)
        except:
            usmjVeze.remove()
            print("Izbacen edge jer nepostoji vrh")

    return listaSusjedstva

def iterative_bfs(graph):

    start, _ = random.choice(list(graph.items()))
    visited = []
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        if v not in visited:
            visited.append(v)
        q.extend(w for w in graph[v] if w not in q and w not in visited)

    return visited

def getKomponente(ls, vrhovi):
    komponente = []
    preostaliVrhovi = vrhovi
    listaSusjeda = ls.copy()
    #dok se ne isprazni iteriraj od svakog elementa i gledaj koje posjeti
    #radi uniju ostalih i posjecenih

    while preostaliVrhovi:
        group = tuple(iterative_bfs(listaSusjeda))
        komponente.append(group)

        preostaliVrhovi = set(tuple(preostaliVrhovi)) - set(group)
        removeNodesFromLS(listaSusjeda, group)

    return komponente

def removeNodesFromLS(listaSusjedstva, nodes):

    for node in nodes:

        del listaSusjedstva[node]

        for k, v in listaSusjedstva.items():
            if node in v:
                tmpV = listaSusjedstva[k]
                tmpV.remove(node)
                listaSusjedstva[k] = tmpV

    return listaSusjedstva

def reverseDicKeyValue(dictionary):
    # :/
    dic = dictionary.copy()
    newDict = dict()

    for k,v in dic.items():
        newDict[v] = k

    return newDict

def getTop5(listaSusjeda, komponente, nodeovi):

    sortiranoPoBrNodeova = sorted(listaSusjeda.items(), key= lambda item : len(item[1]), reverse=True)
    top5NameValue = dict()
    nodes = reverseDicKeyValue(nodeovi)
    cnt = 0

    for v in sortiranoPoBrNodeova:
        compId, companies = v[0], v[1]
        if cnt == 5:
            return top5NameValue
        top5NameValue[nodes[compId]] = len(v[1])
        cnt+=1
    print()

    return top5NameValue

def idVrhova(vrhovi):
    vrhoviID = list()

    for k, v in vrhovi.items():
        vrhoviID.append(v)

    return vrhoviID

def getMax(komponente):
    max = -1
    for i in komponente:
        if max < i.__len__():
            max = i.__len__()
    return max

if __name__ == '__main__':
    vrhovi = dict()
    usmjVeze = list()
    vrhovi, usmjVeze = read("eva.net.txt")

    # print("vrhovi")
    # print(vrhovi)
    # print("arcs")
    # print(usmjVeze)
    # print("lista susjeda")

    ls = convertToListaSusjedstva(usmjVeze)

    vrhoviID = idVrhova(vrhovi)

    # print(ls)

    komponentee = getKomponente(ls, vrhoviID)

    max = getMax(komponentee)

    print("Top 5 companies")
    top = getTop5(ls, komponentee, vrhovi)

    print("firme")
    for k, v in top.items():
        print(k, v)

    print("max number of components ", max, ",percentege ", max/vrhoviID.__len__())
