""" created by stips on 11.10.18. using PyCharm , python_version = 3.5 """

from vjezba1.medak_stipan_zadatak3a import jelProst
# n       1  2  3  4  5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
# prim    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

def ntiProsti(n):

    cnt = 0
    i = 1

    while(cnt < n):
        i+=1
        status, num = jelProst(i)
        if status:
            cnt += 1

            if cnt == n:
                return num

if __name__ == '__main__':

    print(ntiProsti(int(input("Unesi n: "))))

