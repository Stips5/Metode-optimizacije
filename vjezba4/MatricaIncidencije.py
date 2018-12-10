""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

class MatricaIncidencije:
    def __init__(self, vrhovi, edgevi):
        self.vrh = vrhovi
        self.edg = edgevi
        self.matrica = [[0 for x in range(len(edgevi))] for y in range(len(vrhovi))]

    def print(self):

        print("\nMatrica incidencije")
        for r in range(len(self.vrh)):
            for c in range(len(self.edg)):
                print(self.matrica[r][c], end=" ")
            print()
