""" created by stips on 12.12.18. using PyCharm , python_version = 3.5 """

from vjezba4.MatricaSusjedstva import *

class Graf:

    def __init__(self, fileName):
        self.fileName = fileName
        self.keywords = ("*Vertices", "*Arcs", "*Edges")
        self.vrhovi = dict()
        self.neusmjVeze = list()
        self.usmjVeze = list()

        self.read(fileName)

        self.matricaSusjedstva = MatricaSusjedstva(self.vrhovi, self.neusmjVeze, self.usmjVeze)
        self.matricaIncidencije = self.matricaSusjedstva.convertToMatricaIncidencije()
        self.listSusjedstva = self.matricaSusjedstva.convertToListaSusjedstva()


    def getBrojVrhova(self):
        '''redci u matrici incidencije su vrhovi'''
        return len(self.matricaIncidencije.matrica)

    def getBrojBridova(self):
        '''bridovi u matrici incidencije su stupci'''
        return len(self.matricaIncidencije.matrica[0])

    def getStupanjVrha(self):
        '''broj value elemenata liste susjedstva'''
        stupnjeviVrhova = dict()

        for k, v in self.listSusjedstva.lista.items():
            stupnjeviVrhova[k] = len(v)
        return stupnjeviVrhova

    def getVrhoviSaMaxIncidentnihBridova(self):
        '''trazi najduzi valeu iz matrice susjeda'''
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

    def hasEulersPath(self):
        '''Teorem: Konačan, neusmjeren i povezan graf je Eulerov ako i samo ako su su svi vrhovi parnog stupnja'''

        if len(self.usmjVeze) != 0:   #graf je usmjeren, nema eulerov put
            return False

        '''ako stupanj vrha nije paran, graf nema eulerov put'''
        for k, v in self.getStupanjVrha().items():
            if v%2 != 0:
                return False

        return True

    def readVrhovi(self, file, n):
        cnt = 0
        for row in file:
            cnt += 1
            splited = row.replace("\n", "").replace(" ", "").split('"')
            self.vrhovi[splited[1]] = int(splited[0])
            if cnt == n:
                break

    def readUsmjVeze(self, file):
        for row in file:
            if row.__contains__(self.keywords[2]):
                return row
            kae = [int(s) for s in row.split() if s.isdigit()]
            self.usmjVeze.append([kae[0], kae[1]])

    def readNeusmjVeze(self, file):
        for row in file:
            row = row.strip("\n")
            if row == "":
                return row

                # edgevi.append(row.replace("\n", ""))
            '''izdvoji brojeve iz stringa i spremi u listu'''
            kae = [int(s) for s in row.split() if s.isdigit()]
            self.neusmjVeze.append(kae[:2])


    def read(self, fileName):

        file = open(fileName, "r")

        '''cita prvi red i gleda koliko ima tocaka pa svaku tocku ucita'''

        # arcs usmjereni , edge veza

        row = file.readline()
        while row != '':
            row = row.strip("\n")

            '''provjerava jel red u fileu sa headerima da zna di ce spremat'''

            if row.__contains__(self.keywords[0]):  # vrhovi
                n = row.replace(self.keywords[0], "").replace(" ", "")
                self.readVrhovi(file, int(n))
                row = file.readline()
            elif row.__contains__(self.keywords[1]):  # usmjerene veze
                row.replace(self.keywords[1], "").replace(" ", "")
                row = self.readUsmjVeze(file)
            else:
                row.replace(self.keywords[2], "").replace(" ", "")
                self.readNeusmjVeze(file)
                row = file.readline()


