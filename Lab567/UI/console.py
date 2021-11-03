from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
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
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin = input("Dati checkin-ul: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergereRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)


def uiModificareRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Dati noul checkin: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereaRezervarilorLaClasaSuperioara(lista):
    nume = input("Dati numele: ")
    return trecereaRezervarilorLaClasaSuperioara(nume, lista)


def uiIeftinireaRezervarilorCuCheckinCuUnProcentaj(lista):
    procent = int(input("Dati un numar care reprezinta procentul ieftinirii: "))
    return ieftinireaRezervarilorCuCheckinCuUnProcentaj(procent, lista)


def uiPretulMaximPentruFiecareClasa(lista):
    return pretulMaximPentruFiecareClasa(lista)


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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")