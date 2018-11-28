""" created by stips on 10.10.18. using PyCharm Community Edition , python_version = 3.5 """

class Datum:
    def __init__(self, dd, mm):
        self.mnths = (0,31,28,31,30,31,30,31,31,30,31,30,31)

        if dd > 31 or dd < 1:           self.dd = 1
        else:                           self.dd = dd

        if mm > 60 or mm < 0:           self.mm = 0
        else:                           self.mm = mm

    def razlikaDatuma(self, endD):
        razlika = endD.dd - self.dd
        for i in range(self.mm, endD.mm):
            razlika+= self.mnths[i]
        return razlika

class Vrime:
    def __init__(self, sat, minut):

        if sat > 24 or sat < 0:         self.hh = 0
        else:                           self.hh = sat

        if minut > 60 or minut < 0:     self.mm = 0
        else:                           self.mm = minut

    def razlikaVrimena(self, time):
        razlika = (time.hh - self.hh) * 60
        razlika += time.mm - self.mm
        return razlika

class VrimeLeta:

    def __init__(self, zona, vrime, nadnevak):

        if zona > 14 or zona < -12:     self.zona = 0
        else:                           self.zona = zona

        self.time = vrime
        self.date = nadnevak

    def izracunajDuljinuLeta(self, pocetak):
        fLen = 24*60*pocetak.date.razlikaDatuma(self.date)
        fLen += pocetak.time.razlikaVrimena(self.time)
        fLen += 60 * (pocetak.zona - self.zona)
        return fLen

def minuteUSate(len):
    h = len // 60
    min = len - h * 60
    return h, min

def unesiPodatke(pos):

    if pos == 'p':
        pos = 'polaska '
    else:
        pos = 'dolaska '
    zona = int(input("Unesi zonu mjesta " + pos))
    vrime = Vrime(int(input("Unesi sat " + pos)), int(input("Unesi minut " + pos)))
    nadnevak = Datum(int(input("Unesi misec " + pos)), int(input("Unesi dan " + pos)))
    return zona, vrime, nadnevak

if __name__ == '__main__':
    # pocetakLeta = VrimeLeta(0, Vrime(10, 27), Datum(22, 10))
    # krajLeta = VrimeLeta(1, Vrime(12, 28), Datum(22, 10))

    z, v, d = unesiPodatke('p')
    pocetakLeta = VrimeLeta(z, v, d)
    z, v, d = unesiPodatke('k')
    krajLeta = VrimeLeta(z, v, d)

    trajanje = krajLeta.izracunajDuljinuLeta(pocetakLeta)
    h, m = minuteUSate(trajanje)

    print("Trajanje leta je", h, "h ", m, "min")