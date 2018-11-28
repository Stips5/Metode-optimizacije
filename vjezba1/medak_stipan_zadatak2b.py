""" created by stips on 10.10.18. using PyCharm Community Edition , python_version = 3.5 """

from vjezba1.medak_stipan_zadatak2a import *

def trajanjeLeta(vrimeP, zonaP, trajanje, zonaK):
    vrimeP.hh += (zonaK - zonaP)

    h, m = minuteUSate(trajanje)
    vrimeP.hh += h
    vrimeP.mm += m

    return vrimeP

if __name__ == '__main__':
    z = 0
    v = Vrime(10, 27)
    d = Datum(22, 10)
    t = 181
    z_o = 1

    # z, v, d = unesiPodatke('p')
    # t = int(input("Unesi koliko minuta traje let "))
    # z_o = int(input("Unesi vremensku zonu odredista "))

    vrimeDolaska = trajanjeLeta(v, z, t, z_o)
    print("Procjenjeno vrijeme dolaska je" , vrimeDolaska.hh, "h:", vrimeDolaska.mm, "min")


