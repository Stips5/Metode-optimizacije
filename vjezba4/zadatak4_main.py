""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Napisati funkciju koja cita datoteku u kojoj je zapisan graf u pajek formatu i sprema podatke o
# grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije ili listu susjedstva grafa).

if __name__ == '__main__':
    file = open("./euler.net.txt", "r")

    vrhovi = dict()
    edges = list()
    graf = dict()

    fVertices = [next(file) for x in range(6)]

    del fVertices[0]
    for i in fVertices:
        i = i.replace(" ", "")
        i = i.replace("\n", "")
        vrhovi[i[0]] = i[2] + "\t"
    print(vrhovi)

    #pribaci iduca dva retka, file descriptor ili sta vec
    next(file)
    next(file)

    fEdges = [next(file) for y in range(9, 17)]

    for i in fEdges:
        i = i.replace(" ", "")
        i = i.replace("\n", "")
        edges.append(i[0])
        edges.append(i[1])

    for k, v in vrhovi.items():
        for lItem in range(len(edges) - 1):
            if k == edges[lItem]:
                # if edges[lItem] not in
                    #gleda po vrhovima, ako vrh je povezan sa vrhon
                vrhovi[k] += edges[lItem+1]
                vrhovi[k+1] += edges[lItem]


    print("spremljeno")

    for k, v in vrhovi.items():
        print(k, v)