""" created by stips on 10.10.18. using PyCharm Community Edition , python_version = 3.5 """

def trokutarenje(n):

    for i in range(1, n+1):
        zbr = i -1 + i

        for rising in range(i, zbr):
            if rising >= 10:
                print(rising%10, end=" ")
            else:
                print(rising, end=" ")

        for falling in range(zbr, i-1, -1):
            if falling >= 10:
                print(falling%10, end=" ")
            else:
                print(falling, end=" ")

        print()


if __name__ == '__main__':
    # trokutarenje(int(input("Unesi n ")))
    trokutarenje(9)
