""" created by stips on 11.10.18. using PyCharm , python_version = 3.5 """


def getPrimesInRange(upper, lower):
    prosti = list()
    for i in range(upper, lower):
        valid, num = jelProst(i)
        if valid:
            prosti.append(num)

    if prosti[0] == 0:
        prosti.pop(0)
    if prosti[0] == 1:
        prosti.pop(0)

    return prosti

def jelProst(br):
    for j in range(2, br):
        if br % j == 0:
            return False, None
    else:
        return True, br

def prostiBrojeviUFRasponu():
    s_f, e_f = float(input("Unesi donju granicu ")), float(input("Unesi gornju granicu "))

    if s_f < 2:
        s_f = 2

    print(s_f, e_f)

    s = int(s_f)
    e = int(e_f) + 1

    primes = getPrimesInRange(s, e)
    print("U rasponu ima ", primes.__len__(), "primarnih brojeva")

    for i in primes:
        print(i, end=" ")

if __name__ == '__main__':

    prostiBrojeviUFRasponu()
