""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Sest stupnjeva Kevina Bacona je igra u kojoj se za svakog glumca ili glumicu pronalazi Baconov broj odreden sljede´
# cim pravilima:
# • Kevin Bacon ima Baconov broj 0.
# • Baconov broj bilo kojeg drugog glumca ili glumice je minimum Baconovih brojeva svih glumaca ili glumica s kojima je trazeni glumac
# igrao u filmu uvecan za jedan.
# Dan je dataset movies.txt. Koristeci breath-first search napisati program u kojem ce se za unesenog glumca ili glumicu
# pronaci Baconov broj i ispisati putanja kojom je povezan/a sa Kevin Baconom.

#TODO
# iman vrhove, triba provjerit sve vrhove koji imaju isti film i to je veza
import collections
import operator

from vjezba5.myBFS import iterative_bfs as myBFS

if __name__ == '__main__':

    fileName = "movies.txt"
    fileData = open(fileName, "r")

    filmGlumac = dict()
    sviGlumci = list()

    listaSusjedstva = dict()

    graf = dict()

    for i in fileData:

        i = i.replace("\n", "")
        #splitat filmove i glumace
        sveNa2 = i.split(")")

        #splitat filmove
        filmovi = sveNa2[0].split(",")
        filmovi[-1] += ')'

        #splitat glumce
        glumci = sveNa2[1].split(";")
        del glumci[0]       #ostane zarez ko prvi element

        sviGlumci.extend(glumci)

        for i in filmovi:       #dict {film , [glumci]}
            filmGlumac[i] = glumci
    #
    # print("Film glumac")
    # for k, v in filmGlumac.items():
    #     print("key", k, " ||| value", v)

    #inicijalizacija
    for g in sviGlumci:
        listaSusjedstva[g] = None

    #iterira kroz glumce koji glume u filnu i dodaje ih u listu susjedstva
    for k, v in filmGlumac.items():      # k = filmovi , v = glumci
        for glumac in v:
            tmp = list(v)
            tmp.remove(glumac)

            old = listaSusjedstva[glumac]
            if old == None: #ako je prazan value dodaj glumce
                listaSusjedstva[glumac] = tmp
            else:           #ako vec ima glumaca, dodaj na postojece
                # new = old.extend(tmp)
                listaSusjedstva.setdefault(glumac, []).extend(tmp)


            #triba nandodat na vec postojece podatke

    print("")

    listaSusjedstva = collections.OrderedDict(sorted(listaSusjedstva.items()))
    # for k, v in listaSusjedstva.items():
    #     print(k, v)
    #
    # actors, baconNum = myBFS(listaSusjedstva,  "Kevin Bacon")
    # print("Actors", actors, "Bacons number", baconNum)
    #
    actors, baconNum = myBFS(listaSusjedstva,  "Brad Pitt")
    # print("Actors", actors, "Bacons number", baconNum)

    # actors, baconNum = myBFS(listaSusjedstva, "Z. Zakowsky")
    if actors == None:
        print("No connection")

    else:
        print()

        cntEdges = 0

        for i in range(len(actors)-1):
            for f, g in filmGlumac.items():
                if(g.__contains__(actors[i]) and g.__contains__(actors[i+1])):
                    print(actors[i] , "->", f, "->", actors[i+1])


        print()

        print("Actors", actors, "Bacons number", baconNum)
