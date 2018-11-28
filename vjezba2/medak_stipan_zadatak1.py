""" created by stips on 24.10.18. using PyCharm , python_version = 3.5 """

def iterativnoNajveci(lista, maks = -99999):

    for i in range(lista.__len__()):
        if isinstance(lista[i], int):
            if lista[i] > maks:
                maks = lista[i]
    return maks

def rekurzivnoNajveci(lista, maks = -9999, i = 0):
    if i == lista.__len__():
        return maks
    # if isinstance(lista[i], int):
    if type(lista[i]) is int:
        if lista[i] > maks:
            maks = lista[i]
    i+=1
    return rekurzivnoNajveci(lista, maks, i)


if __name__ == '__main__':
    lst = [7, 18, 3, 'a', True, (2, 3)]
    import time

    # start1 = time.time()
    print("Iterativno najveci ", iterativnoNajveci(lst))
    # end1 = time.time()
    # print("iteracija", (end1 - start1))

    # start = time.time()
    print("Rekurzivno najveci ", rekurzivnoNajveci(lst))
    # end = time.time()
    # print("moj rekurzan", (end - start))
