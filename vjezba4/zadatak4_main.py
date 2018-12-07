""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Napisati funkciju koja cita datoteku u kojoj je zapisan graf u pajek formatu i sprema podatke o
# grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije ili listu susjedstva grafa).

class MatricaSusjedstva:

    def __init__(self, fileName):
        self.graf = dict()
        self.matrica = None
        self.fileName = fileName
        self.keywords = ("*Vertices", "*Arcs", "*Edges")

        data = self.read(self.fileName)

    def read(self, fileName):
        vrhovi = dict()
        edges = dict()
        edgevi = list()
        arcovi = list()

        file = open(fileName, "r")
        '''cita prvi red i gleda koliko ima tocaka
        pa svaku tocku ucita'''

    #arcs usmjereni , edge veza

        file1 = open(fileName, "r")

        for i, line in enumerate(file1):
            print(i, line)

        for row in file:
            '''
                provjerava jel red u fileu sa headerima da zna di ce spremat
            '''

            row = row.replace("\n", "")
            if row.__contains__(self.keywords[0]):     #vrhovi
                row = row.replace(self.keywords[0], "").replace(" ", "")
                nRows = int(row)
                row = next(file)
                for i in range(nRows):
                    splited = row.replace("\n", "").replace(" ", "").split('"')
                    vrhovi[splited[1]] = splited[0]
                    row = next(file)

            elif row.__contains__(self.keywords[1]):   #lukovi
                while True:
                    row = next(file)
                    if row.__contains__(self.keywords[2]):
                        break
                    else:
                        arcovi.append(row.replace("\n", ""))
            else:
                while True:
                    row = next(file, 0)
                    if row == 0:
                        break
                    else:
                        edgevi.append(row.replace("\n", ""))

        print("spremljeno")

        print("Vrhovi")
        for k, v in vrhovi.items():
            print(k, v)

        print("Arcovi")
        for i in arcovi:
            print(i)

        print("Edgevi")
        for i in edgevi:
            print(i)

if __name__ == '__main__':
        # fileName = "euler.net.txt"
        fileName = "football.net.txt"

        MatricaSusjedstva(fileName)
