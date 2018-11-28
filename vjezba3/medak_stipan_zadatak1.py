""" created by stips on 14.11.18. using PyCharm , python_version = 3.5 """
import time

import pandas as panda

def zadatak1():
    '''
    1. Napisati funkciju koja će pročitati datoteku i u drugu datoteku zapisati OZV ljudi u periodima od po 10 godina,
    tako da zadnja godina bude 2016. godina (1806., 1816.,..,2016.).
    Pritom treba izbaciti one države koje nemaju podatke za sve tražene godine.
    :return:
    '''

    try:
        df = panda.read_csv("life.csv")
    except:
        print("File nije ucitan!")
        exit()

    start = time.time()

    '''dobit zadnju godinu tj stupac'''
    lastYear = int(df.columns[-1])

    lista = []

    '''ispis svako 10 godina'''
    for year in range(lastYear, 1800, -10):
        lista.append(str(year))

    '''nmz se radit reverse liste pa san ovako uradia reverse, Life expectancy doda države'''
    nList = ['Life expectancy']
    for i in range(len(lista) -1 , 0, -1):
        nList.append(lista[i])

    '''kopira stupce od ovih svako 10i iz liste'''
    nf = df[nList].copy()

    '''izbaci one koji nemaju podatke i spremi u file'''
    nf = panda.DataFrame(nf.dropna())

    end = time.time()
    print("Zadatak 1, vrijeme izvođenja", (end - start) * 1000, "ms")

    nf.to_csv("svaki_10ti_bez_Nan.csv")