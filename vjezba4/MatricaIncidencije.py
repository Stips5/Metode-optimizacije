""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

class MatricaIncidencije:
    def __init__(self, vrhovi, edgevi):
        self.vrh = vrhovi
        self.edg = edgevi
        self.matrica = self.initMatrix()

    def initMatrix(self):
        return [[0 for x in range(len(self.edg))] for y in range(len(self.vrh))]

    def print(self):

        print("\nMatrica incidencije")
        for r in range(len(self.vrh)):
            for c in range(len(self.edg)):
                print(self.matrica[r][c], end=" ")
            print()
