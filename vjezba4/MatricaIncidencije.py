""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

class MatricaIncidencije:
    def __init__(self, vrhovi, edgevi, arcs):
        self.vrh = vrhovi
        self.edg = edgevi
        self.arc = arcs
        self.matrica = self.initMatrix()

    def initMatrix(self):
        if len(self.edg) != 0:
            return [[0 for x in range(len(self.edg))] for y in range(len(self.vrh))]
        else:
            return [[0 for x in range(len(self.arc))] for y in range(len(self.vrh))]

    def print(self):

        print("\nMatrica incidencije")

        if len(self.edg) != 0:
            for r in range(len(self.vrh)):
                for c in range(len(self.edg)):
                    print(self.matrica[r][c], end=" ")
                print()
        else:
            for r in range(len(self.vrh)):
                for c in range(len(self.arc)):
                    print(self.matrica[r][c], end=" ")
                print()

