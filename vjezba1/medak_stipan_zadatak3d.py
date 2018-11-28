""" created by stips on 11.10.18. using PyCharm , python_version = 3.5 """

from vjezba1.medak_stipan_zadatak3a import jelProst

if __name__ == '__main__':

    uneseniBroj = int(input("Unesi paran broj "))

    if uneseniBroj%2 != 0:
        print("Uneseni broj nije paran ")

    prosti = list()

    #prosti brojevi u rangeu
    for i in range(2, uneseniBroj):
        status, br = jelProst(i)

        if status:
            prosti.append(i)

    #kobiniranje brojeva
    goldbachoveSlutnje = list()

    for i in range(prosti.__len__()):
        for j in range(prosti.__len__()):
            if prosti[i] + prosti[j] == uneseniBroj:
                goldbachoveSlutnje.append(str(prosti[i]) + "+" + str(prosti[j]) + "=" + str(uneseniBroj))

    print(goldbachoveSlutnje)