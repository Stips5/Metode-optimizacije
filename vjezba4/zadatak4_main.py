""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Napisati funkciju koja cita datoteku u kojoj je zapisan graf u pajek formatu i sprema podatke o
# grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije ili listu susjedstva grafa).

from vjezba4.Graf import Graf

if __name__ == '__main__':

    fileName = "euler.net.txt"
    # fileName = "football.net.txt"

    # TODO
    # eulerov test ?!?

    #učitavanje filea u graf
    graf = Graf(fileName)

    ms = graf.matricaSusjedstva
    ms.print()

    ls = graf.listSusjedstva
    ls.print()

    mi = graf.matricaIncidencije
    mi.print()


    print("br bridova", graf.getBrojBridova())

    print("br vrhova", graf.getBrojVrhova())

    print("stupanj vrhova", graf.getStupanjVrha())

    print("max br vrhova", graf.getVrhoviSaMaxIncidentnihBridova())

    print("Ima li Eulerov put: ", 'Ima' if graf.hasEulersPath() else 'Nema')
