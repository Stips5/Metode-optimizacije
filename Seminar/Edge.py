""" created by stips on 15.01.19. using PyCharm , python_version = 3.5 """

class Edge:
    def __init__(self, n1, n2, length, cost):
        self.node1 = n1
        self.node2 = n2
        self.length = length
        self.cost = cost

    def __str__(self):
        return str(self.node1) + "---" + str(self.node2) + " len=" + str(self.length) + " cost=" + str(self.cost)

