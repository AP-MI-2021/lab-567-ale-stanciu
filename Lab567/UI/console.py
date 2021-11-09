from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare, getById
from Logic.functionalitati import trecereaRezervarilorLaClasaSuperioara, ieftinireaRezervarilorCuCheckinCuUnProcentaj, \
    pretulMaximPentruFiecareClasa


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă")
    print("a. Afisare toate rezervarile")
    print("x. Iesire")


def uiAdaugareRezervare(lista):
    try:
        id = input("Dati id-ul (un numar intreg): ")
        nume = input("Dati numele: ")
        while True:
            clasa = input("Dati clasa (economy / economy plus / business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Ati introdus o clasa inexistenta!")
            else:
                break
        while True:
            try:
                pret = float(input("Dati pretul (un numar real): "))
            except ValueError as ve:
                print("Ati introdus o valoare gresita!")
            else:
                break
        while True:
            checkin = input("Dati noul checkin (da / nu): ")
            if checkin != "da" and checkin != "nu":
                print("Ati introdus un checkin gresit!")
            else:
                break
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        if getById(id, lista) is None:
            raise ValueError("Id-ul nu exista")
        else:
            return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        while True:
            clasa = input("Dati noua clasa: ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Ati introdus o clasa inexistenta!")
            else:
                break
        while True:
            try:
                pret = float(input("Dati pretul (un numar real): "))
            except ValueError as ve:
                print("Ati introdus o valoare gresita!")
            else:
                break
        while True:
            checkin = input("Dati noul checkin (da / nu): ")
            if checkin != "da" and checkin != "nu":
                print("Ati introdus un checkin gresit!")
            else:
                break
        return modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereaRezervarilorLaClasaSuperioara(lista):
    try:
        nume = input("Dati numele: ")
        return trecereaRezervarilorLaClasaSuperioara(nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinireaRezervarilorCuCheckinCuUnProcentaj(lista):
    try:
        procent = int(input("Dati un numar care reprezinta procentul ieftinirii: "))
        return ieftinireaRezervarilorCuCheckinCuUnProcentaj(procent, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretulMaximPentruFiecareClasa(lista):
    try:
        return pretulMaximPentruFiecareClasa(lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificareRezervare(lista)
        elif optiune == "4":
            lista = uiTrecereaRezervarilorLaClasaSuperioara(lista)
        elif optiune == "5":
            lista = uiIeftinireaRezervarilorCuCheckinCuUnProcentaj(lista)
        elif optiune == "6":
            print(uiPretulMaximPentruFiecareClasa(lista))
        elif optiune == "7":
            pass
        elif optiune == "8":
            pass
        elif optiune == "9":
            pass
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")