""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Napisati funkciju koja cita datoteku u kojoj je zapisan graf u pajek formatu i sprema podatke o
# grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije ili listu susjedstva grafa).

from vjezba4.MatricaSusjedstva import MatricaSusjedstva

if __name__ == '__main__':
        fileName = "euler.net.txt"
        # fileName = "football.net.txt"

        ms = MatricaSusjedstva(fileName)

        # print(len(ms.matrica[0]))

        ms.print()


        ls = ms.convertToListaSusjedstva()

        ls.print()


        mi = ms.convertToMatricaIncidencije()
        mi.print()