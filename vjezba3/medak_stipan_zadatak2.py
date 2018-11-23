""" created by stips on 23.11.18. using PyCharm , python_version = 3.5 """

import pandas as panda

def zadatak2(godina):
    '''
        2. Napisati funkciju koja će za odredenu godinu (godina je parametar funkcije) sortirati
        države sortirati po OZV-u, od većeg prema manjem broju.
        :return:
    '''

    df = panda.read_csv("svaki_10ti_bez_Nan.csv")

    rowNum = df.shape[0]
    lastYear = int(df.columns[-1])
    firstYear = int(df.columns[1])

    print("lastYear", lastYear, " ", "firstYear", firstYear)

    # for county in range(rowNum):
    #     print(df["Life expectancy"][county])

    try:

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