""" created by stips on 23.11.18. using PyCharm , python_version = 3.5 """

import pandas as panda

def zadatak3():
    '''3.
        Napisati funkciju koja traži države u kojima je OŽV pao u dvije susjedne godine,
        te broji koliko puta je pao.'''


    '''nean pojma tribat ce for{for{}}'''

    df = panda.read_csv("svaki_10ti_bez_Nan.csv")

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
