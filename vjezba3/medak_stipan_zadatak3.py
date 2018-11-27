""" created by stips on 23.11.18. using PyCharm , python_version = 3.5 """
import operator
import os
import time

import pandas as panda

def zadatak3():
    '''3.
        Napisati funkciju koja traži države u kojima je OŽV pao u dvije susjedne godine,
        te broji koliko puta je pao.'''

    df = panda.read_csv("svaki_10ti_bez_Nan.csv")

    start = time.time()

    repeats = dict()

    for country in df.iterrows():       #Serial di su redci indeksirani ko godine
        cnt = 0
        # index 0 je header neki, index 1 ime drzave, ostalo su podatci po godinama
        for i in range(2, len(country[1])-2):
            if ((country[1][i] > country[1][i+1]) and country[1][i+1] > country[1][i+2]):
                cnt += 1

        repeats[country[1][1]] =+ cnt

    end = time.time()
    print("Zadatak 3, vrijeme izvođenja", (end-start) * 1000, "ms")

    fileName = "padovi_drzava.txt"
    file = open(fileName, "w+")

    for k, v in sorted(repeats.items(), key=operator.itemgetter(1)):
        # print(k, v)
        file.write(str(k) + " " + str(v))
        file.write("\n")
    print("File saved as", os.getcwd() + "/" + fileName)
