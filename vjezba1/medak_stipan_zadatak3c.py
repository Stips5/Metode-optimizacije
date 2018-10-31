""" created by stips on 11.10.18. using PyCharm , python_version = 3.5 """

from vjezba1.medak_stipan_zadatak3a import jelProst

def getSusjedniProsti(limit):
    prosti = list()

    for i in range(limit):
        primFlag, br = jelProst(i)

        if primFlag:
            prosti.append(br)

    susjedni = list()

    for i in range(prosti.__len__()-1):
        next = prosti[i + 1]
        tmp = prosti[i]
        if (next - tmp) == 2:
            if tmp in susjedni:
                continue
            else:
                susjedni.append(tmp)
                susjedni.append(next)

    print(susjedni)

    return susjedni

if __name__ == '__main__':

    upperLmt = int(input("Unesi gornju granicu "))

    getSusjedniProsti(upperLmt)


