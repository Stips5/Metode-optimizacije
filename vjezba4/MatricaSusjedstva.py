""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

from vjezba4.MatricaIncidencije import MatricaIncidencije
from vjezba4.ListaSusjedstva import ListaSusjedstva

class MatricaSusjedstva:

    def __init__(self, fileName):
        self.graf = dict()
        self.matrica = None
        self.fileName = fileName
        self.keywords = ("*Vertices", "*Arcs", "*Edges")
        self.vrhovi = dict()
        self.edges = list()
        self.arcovi = list()

        self.read(fileName)

    def read(self, fileName):

        file = open(fileName, "r")

        '''cita prvi red i gleda koliko ima tocaka pa svaku tocku ucita'''

        #arcs usmjereni , edge veza

        for row in file:
            '''
                provjerava jel red u fileu sa headerima da zna di ce spremat
            '''

            row = row.replace("\n", "")
            if row.__contains__(self.keywords[0]):     #vrhovi
                row = row.replace(self.keywords[0], "").replace(" ", "")
                nRows = int(row)
                cnt = 0
                for row in file:
                    cnt+=1
                    splited = row.replace("\n", "").replace(" ", "").split('"')
                    self.vrhovi[splited[1]] = int(splited[0])
                    if cnt == nRows:
                        break

            elif row.__contains__(self.keywords[1]):   #lukovi
                for row in file:
                    if row.__contains__(self.keywords[2]):
                        break
                    self.arcovi.append(row.replace("\n", ""))
            else:
                for row in file:
                    if row == 0:
                        break

                        # edgevi.append(row.replace("\n", ""))
                    kae = [int(s) for s in row.split() if s.isdigit()]
                    self.edges.append(kae[:2])

        self.matrica = [[0 for x in range(len(self.vrhovi))] for y in range(len(self.vrhovi))]

        for e in self.edges:
            i1, i2 = e[0], e[1]
            self.matrica[i1-1][i2-1] += 1
            self.matrica[i2-1][i1-1] += 1

    def print(self):
        print("\nMatrica susjedstva")
        for r in range(5):
            for c in range(5):
                print(self.matrica[r][c], end=" ")
            print()

    def convertToListaSusjedstva(self):
        ls = ListaSusjedstva()

        for k,v in self.vrhovi.items():
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
