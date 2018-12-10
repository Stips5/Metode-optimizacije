""" created by stips on 10.12.18. using PyCharm , python_version = 3.5 """

class ListaSusjedstva:
    def __init__(self):
        self.lista = dict()

    def print(self):
        print("\nLista susjedstva")
        for k, v in self.lista.items():
            print(k, v)