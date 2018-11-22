""" created by stips on 14.11.18. using PyCharm , python_version = 3.5 """

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

    columnNum = df.shape[1]
    rowNum = df.shape[0]

    print("num of rows", rowNum, " num of columns", columnNum)

    lastYear = int(df.columns[-1])

    # print(type(lastYear), lastYear)
    # print("df ly", df[str(lastYear)])

    '''ispisiva godine'''
    # for year in range(lastYear, 1800, -1):
    #     # print(df[str(year)], end=" ")
    #     # print(df[0][year], end=" ")
    #     print(df[str(year)])

    '''ispis drzava'''
    # print(df['Life expectancy'])

    lista = list()

    # '''ispis svako 10 godina'''
    # for year in range(lastYear, 1800, -10):
    #     # print(df[str(year)], end=" ")
    #     # print(df[0][year], end=" ") ne radi
    #     # print("year", year, "\n", df[str(year)])
    #
    #     # if df[str(year)].__contains__(nmpy.NaN):
    #     pass


    # print(df.dropna())

    '''new file, nf without Nan's'''

    nf = panda.DataFrame(columns=["1800","1000"], index=[1,2,3,4])


    '''vidit kao kopirat stupac iz df u df'''

    for year in range(lastYear, 1800, -10):
        nf.append(df[str(year)])


    # nf = panda.DataFrame(nf.dropna())
    # nf.to_csv("svaki_10ti_bez_Nan.csv")


    print(nf)

    # if df[df[str(year)].__contains__(df.isnull)]:
    #     lista.append(df[str(year)])


    print(lista)


    # radi print(df['2012'][1])

def zadatak2(godina):
    '''
        2. Napisati funkciju koja će za odredenu godinu (godina je parametar funkcije) sortirati
        države sortirati po OZV-u, od većeg prema manjem broju.
        :return:
    '''

    df = panda.read_csv("life.csv")


    rowNum = df.shape[0]
    # lastYear = int(df.columns[-1])
    # firstYear = int(df.columns[1])

    # for county in range(rowNum):
    #     print(df["Life expectancy"][county])


    df.sort_values(str(godina), ascending=False, inplace=True)
    print(df[str(godina)])


    '''uradit jos da ostavi samo drzave i OŽV po kojima je sortiran
    sad sortira dobro al ostavi sve ostale tj cili DataFrame
    i provjeri jel godina koja se unese u DataFrameu'''

    # print(df)
    # print(df[str(godina)])
    #
    # if godina >= 1800 and godina <= 2016:
    #     return
    #
    # for year in range(1800, 2016):
    #     print(df[str(year)])

def zadatak3():
    '''3.
        Napisati funkciju koja traži države u kojima je OŽV pao u dvije susjedne godine,
        te broji koliko puta je pao.'''


    '''nean pojma tribat ce for{for{}}'''

    df = panda.read_csv("life.csv")

    columnNum = df.shape[1]

    lastyear= int(df.columns[-1])

    print(lastyear)

    for i in range(1800, lastyear):
        print("year", i)

        print(df[str(i)])

        if (df[str(i+1)] > df[str(i)]) and (df[str(i+2)] > df[str(i+1)]):
            print("ima")
            # print("Ima ode nesto ", df[str(i)], df[str(i+1)], df[str(i+2)])


        # if (df[i+1] > df[i]) and (df[i+2] > df[i+1]):
        #     print("Ima ode nesto ", df[i], df[i+1], df[i+2])

if __name__ == '__main__':
    # zadatak1()
    # zadatak2(2000)
    # zadatak3()
    pass