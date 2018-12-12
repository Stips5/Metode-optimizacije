""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

from vjezba4.MatricaIncidencije import MatricaIncidencije
from vjezba4.ListaSusjedstva import ListaSusjedstva

class MatricaSusjedstva:

    def __init__(self, vrhovi, edges, matrica):
        self.vrhovi = vrhovi
        self.edges = edges
        self.matrica = matrica

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
        mi = MatricaIncidencije(self.vrhovi, self.edges)

        for e in range(len(self.edges)):
            e1, e2 = self.edges[e][0], self.edges[e][1]
            mi.matrica[e1-1][e] += 1
            mi.matrica[e2-1][e] += 1

        return mi

    def print(self):
        print("\nMatrica susjedstva")
        for r in range(5):
            for c in range(5):
                print(self.matrica[r][c], end=" ")
            print()