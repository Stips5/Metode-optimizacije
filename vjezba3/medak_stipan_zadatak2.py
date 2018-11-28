""" created by stips on 23.11.18. using PyCharm , python_version = 3.5 """
import time

import pandas as panda


def zadatak2(godina):
    '''
        2. Napisati funkciju koja će za odredenu godinu (godina je parametar funkcije) sortirati
        države sortirati po OZV-u, od većeg prema manjem broju.
        :return:
    '''

    df = panda.read_csv("svaki_10ti_bez_Nan.csv")

    try:
        '''
            sortiranje po godini
            ako godina koja je unesena ne postoji ide na except
        '''

        start = time.time()

        df.sort_values(str(godina), ascending=False, inplace=True)

        end = time.time()
        print("Zadatak 2, vrijeme izvođenja", (end-start) * 1000, "ms")

        df.to_csv("sortiranoPoGodini.csv")
    except:
        print("Godina ne postoji u fileu")
