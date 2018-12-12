""" created by stips on 12.12.18. using PyCharm , python_version = 3.5 """

from vjezba4.MatricaSusjedstva import *

class Graf:

    def __init__(self, fileName):
        self.graf = dict()
        self.matrica = None
        self.fileName = fileName
        self.keywords = ("*Vertices", "*Arcs", "*Edges")
        self.vrhovi = dict()
        self.edges = list()
        self.arcovi = list()

        self.read(fileName)

        self.matricaSusjedstva = MatricaSusjedstva(self.vrhovi, self.edges, self.matrica)
        self.matricaIncidencije = self.matricaSusjedstva.convertToMatricaIncidencije()
        self.listSusjedstva = self.matricaSusjedstva.convertToListaSusjedstva()


    def getBrojVrhova(self):
        return len(self.matricaIncidencije.matrica)

    def getBrojBridova(self):
        return len(self.matricaIncidencije.matrica[0])

    def getStupanjVrha(self):
        stupnjeviVrhova = dict()

        for k, v in self.listSusjedstva.lista.items():
            stupnjeviVrhova[k] = len(v)
        return stupnjeviVrhova

    def getVrhoviSaMaxIncidentnihBridova(self):
        maximusi = dict()

        maxi = -1
        maxKey = 1
        for k, v in self.getStupanjVrha().items():
            if v > maxi:
                maxi = v
                maxKey = k


        for k, v in self.listSusjedstva.lista.items():
            if maxKey == k:
                maximusi[k] = v

        return maximusi

    def read(self, fileName):
        file = open(fileName, "r")

        '''cita prvi red i gleda koliko ima tocaka pa svaku tocku ucita'''

        # arcs usmjereni , edge veza

        for row in file:
            '''
                provjerava jel red u fileu sa headerima da zna di ce spremat
            '''

            row = row.replace("\n", "")
            if row.__contains__(self.keywords[0]):  # vrhovi
                row = row.replace(self.keywords[0], "").replace(" ", "")
                nRows = int(row)
                cnt = 0
                for row in file:
                    cnt += 1
                    splited = row.replace("\n", "").replace(" ", "").split('"')
                    self.vrhovi[splited[1]] = int(splited[0])
                    if cnt == nRows:
                        break

            elif row.__contains__(self.keywords[1]):  # lukovi
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
            self.matrica[i1 - 1][i2 - 1] += 1
            self.matrica[i2 - 1][i1 - 1] += 1

