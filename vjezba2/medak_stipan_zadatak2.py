""" created by stips on 24.10.18. using PyCharm , python_version = 3.5 """

def iterativnaOkretaljka(lista, start, stop):
    '''
    funkcija okrece elemente od startanog indeksa do stop indeksa nad elementima liste lista
    for petlja do onoliko clanova koliko elementa ima izmedeu indeksa / 2
    :param lista:
    :param start:
    :param stop:
    :return:
    '''
    for i in range((stop-start+1)//2):
        lista[start+i], lista[stop-i] = lista[stop-i], lista[start+i]
    return lista

def rekurzivnaOkretaljkaNoSlice(lista, start, stop, i = 0):
    '''
    uvjet izlaska je da je prijedeno pola puta u rasponu
    inace prebacuj elemente i kreci se listom
    :param lista:
    :param start:
    :param stop:
    :param i:
    :return:
    '''
    if i == (stop - start + 1) // 2:
        return lista
    lista[start:start + i:], lista[stop:stop - i] = lista[stop:stop - i], lista[start:start + i]
    i += 1
    return rekurzivnaOkretaljkaSlice(lista, start, stop, i)

def rekurzivnaOkretaljkaSlice(lista, start, stop, i=0):
    '''
    uvjet izlaska je da je prijedeno pola puta u rasponu
    inace prebacuj elemente i kreci se listom
    :param lista: 
    :param start: 
    :param stop: 
    :param i: 
    :return: 
    '''
    if i == (stop-start+1)//2:
        return lista
    lista[start+i], lista[stop-i] = lista[stop-i], lista[start+i]
    i+=1
    return rekurzivnaOkretaljkaSlice(lista, start, stop, i)

if __name__ == '__main__':
    lst = [2, 4, 6, 3, 9, 'a']

    print("Orginal", lst)

    print("Interativly swapped", iterativnaOkretaljka(lst, 1, 4))
    print("Recursivly swapped", rekurzivnaOkretaljkaNoSlice(lst, 1, 4))
    print("Recursivly slicley swapped", rekurzivnaOkretaljkaSlice(lst, 1, 4))

