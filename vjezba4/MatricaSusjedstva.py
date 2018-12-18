""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

from vjezba4.MatricaIncidencije import MatricaIncidencije
from vjezba4.ListaSusjedstva import ListaSusjedstva

class MatricaSusjedstva:

    def __init__(self, vrhovi, edges, arcs):
        self.vrhovi = vrhovi
        self.edges = edges
        self.arcs = arcs
        self.matrica = self.initMatrix()

        '''idi po stupcima i dodaj redke iz uredenog para'''

        if len(self.edges) != 0:
            for e in self.edges:
                i1, i2 = e[0], e[1]
                self.matrica[i1 - 1][i2 - 1] += 1
                self.matrica[i2 - 1][i1 - 1] += 1
        else:
            for a in self.arcs:
                i1, i2 = a[0], a[1]
                self.matrica[i1 - 1][i2 - 1] += 1
                self.matrica[i2 - 1][i1 - 1] += 1


    def initMatrix(self):
        return [[0 for x in range(len(self.vrhovi))] for y in range(len(self.vrhovi))]

    def convertToListaSusjedstva(self):
        ls = ListaSusjedstva()

        for k, v in self.vrhovi.items():
            ls.lista[v] = None

        for c in range(len(self.matrica[0])):
            lista = list()
            for r in range(len(self.matrica[0])):
                if self.matrica[r][c] == 1:
                    lista.append(r+1)
            ls.lista[c+1] = lista

        return ls

    def convertToMatricaIncidencije(self):
        mi = MatricaIncidencije(self.vrhovi, self.edges, self.arcs)

        leng = len(mi.matrica[0])

        '''stupac po stupac gleda i one edgeve koje ima doda'''

        if len(self.edges) != 0:
            for e in range(len(self.edges)):
                e1, e2 = self.edges[e][0], self.edges[e][1]
                mi.matrica[e1-1][e] += 1
                mi.matrica[e2-1][e] += 1
        else:
            for a in range(len(self.arcs)):
                a1, a2 = self.arcs[a][0], self.arcs[a][1]
                mi.matrica[a1-1][a] += 1
                mi.matrica[a2-1][a] += 1

        return mi

    def print(self):
        print("\nMatrica susjedstva")
        for r in range(len(self.vrhovi)):
            for c in range(len(self.vrhovi)):
                print(self.matrica[r][c], end=" ")
            print()