""" created by stips on 24.10.18. using PyCharm , python_version = 3.5 """
import os
header = ''

class Evidencija:
    def __init__(self, unos):

        self.matBr = unos[0]
        self.status = unos[1]
        self.kod = unos[2]

        # if isinstance(unos[3], int):
        if str(unos[3]).isnumeric():
            self.vjezbe = int(unos[3])
        else:
            self.vjezbe = int(0)

        # if isinstance(unos[4], int):
        if str(unos[4]).isnumeric():
            self.k1 = int(unos[4])
        else:
            self.k1 = int(0)

        # if isinstance(unos[5], int):
        if str(unos[5]).isnumeric():
            self.k2 = int(unos[5])
        else:
            self.k2 = int(0)

        # if isinstance(unos[6], int):
        if str(unos[6]).isnumeric():
            self.rok1 = int(unos[6])
        else:
            self.rok1 = int(0)

        self.flag = ''

    def print(self):
        '''
        funkcija koja ispisiva atribute objekta
        :return:
        '''
        print("Mat. br", self.matBr, ", status", self.status, ", kod",  self.kod, ", vjezbe", str(self.vjezbe),  ", kol1", str(self.k1), ", kol1", str(self.k2), ", rok1", str(self.rok1))

    def getWriteFormated(self):
        '''
        funkcija vraca atribute objekta spremne za upis u file
        :return:
        '''
        return self.matBr + "," + self.status + "," + self.kod + "," + str(self.vjezbe) + "," + str(self.k1) + "," + str(self.k2) + "," + str(self.rok1) + "," + str(self.flag)

def ucitavanjeFilea():
    '''
    ucitavanje iz filea i dodavanje u listu kao objekt tipa Evidencija
    prvo ucitavanje ne spremi korisne podatke vec header,
    funkcija vraca listu objekata
    :return:
    '''
    try:
        file = open("evidencija.csv")
    except:
        print("File nije ucitan!")
        exit()

    podatci = list()

    cnt = 0
    for i in file:
        if cnt == 0:
            global header
            header = i
        else:
            podatci.append(Evidencija(i.split(',')))
        cnt += 1

    print("Podatci ucitani")
    return podatci

def upisivanjeUFile(podatci):
    '''
    funkcija otvara file i upisiva u njega listu objekata, ukljucujuci header
    :param podatci:
    :return:
    '''
    fileName = "evidencija_final.csv"
    file = open(fileName, "w+")

    file.write(header)

    for i in podatci:
        file.write(i.getWriteFormated())
        file.write("\n")

    print("File saved as", os.getcwd() + "/" +fileName)

def provjeraStudenata(podatci):
    '''
    funkcija provjerava je li student polozio ako je dodjeljuje mu postotak
    dodaje objektu vrijednost
    :param podatci:
    :return:
    '''
    for i in range(podatci.__len__()):
        if podatci[i].vjezbe < 50:
            podatci[i].flag = 'NOOP'
        else:
            podatci[i].flag = round(izracunajBrojBodova(podatci[i]),2)
    return podatci

def izracunajBrojBodova(student):
    '''f-ja racuna broj bodova'''
    if student.k1 >= 40 and student.k2 >= 40:
        return 0.2 * student.vjezbe + 0.4 * student.k1 + 0.4 * student.k2
    elif student.rok1 >= 50:
        return 0.2 * student.vjezbe + 0.8 * student.rok1
    else:
        return 1

if __name__ == '__main__':

    upisivanjeUFile(provjeraStudenata(ucitavanjeFilea()))


