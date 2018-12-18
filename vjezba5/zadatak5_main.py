""" created by stips on 28.11.18. using PyCharm , python_version = 3.5 """

# Sest stupnjeva Kevina Bacona je igra u kojoj se za svakog glumca ili glumicu pronalazi Baconov broj odreden sljede´
# cim pravilima:
# • Kevin Bacon ima Baconov broj 0.
# • Baconov broj bilo kojeg drugog glumca ili glumice je minimum Baconovih brojeva svih glumaca ili glumica s kojima je trazeni glumac igrao u filmu uvecan za jedan.
# Dan je dataset movies.txt. Koristeci breath-first search napisati program u kojem ´
# ce se za unesenog glumca ili glumicu pronaci Baconov broj i ispisati putanja kojom je povezan/a sa Kevin Baconom.

#TODO
# iman vrhove, triba provjerit sve vrhove koji imaju isti film i to je veza

if __name__ == '__main__':

    fileName = "movies.txt"
    fileData = open(fileName, "r")

    filmGlumac = dict()
    sviGlumci = list()

    graf = dict()

    for i in fileData:

        i = i.replace("\n", "")
        sveNa2 = i.split(")")

        filmovi = sveNa2[0].split(",")
        filmovi[-1] += ')'
        glumci = sveNa2[1].split(";")
        del glumci[0]

        sviGlumci.extend(glumci)

        for i in filmovi:
            filmGlumac[i] = glumci

    for k, v in filmGlumac.items():
        print("key", k, " ||| value", v)




    for glumac in sviGlumci:
        for film, glumci in filmGlumac.items():
            if glumac in glumci:
                glumci.remove(glumac)
                graf[glumac] = graf[glumac].extend(glumci)


    print("\nSito i rešeto")
    for k, v in graf.items():
        print(k, v)