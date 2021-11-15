from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare, getById
from Logic.functionalitati import trecereaRezervarilorLaClasaSuperioara, ieftinireaRezervarilorCuCheckinCuUnProcentaj, \
    pretulMaximPentruFiecareClasa, ordonareDescrescatorDupaPret, sumePreturiPerNume


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare toate rezervarile")
    print("x. Iesire")


def uiAdaugareRezervare(lista, undoList, redoList):
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
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        if getById(id, lista) is None:
            raise ValueError("Id-ul nu exista")
        else:
            rezultat = stergeRezervare(id, lista)
            undoList.append(lista)
            redoList.clear()
            return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareRezervare(lista, undoList, redoList):
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
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereaRezervarilorLaClasaSuperioara(lista, undoList, redoList):
    try:
        nume = input("Dati numele: ")
        rezultat = trecereaRezervarilorLaClasaSuperioara(nume, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinireaRezervarilorCuCheckinCuUnProcentaj(lista, undoList, redoList):
    try:
        procent = int(input("Dati un numar care reprezinta procentul ieftinirii: "))
        rezultat = ieftinireaRezervarilorCuCheckinCuUnProcentaj(procent, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretulMaximPentruFiecareClasa(lista):
    try:
        return pretulMaximPentruFiecareClasa(lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiOrdonareDescrescatorDupaPret(lista):
    showAll(ordonareDescrescatorDupaPret(lista))


def uiSumePreturiPerNume(lista):
    try:
        rezultat = sumePreturiPerNume(lista)
        for nume in rezultat:
            print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificareRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiTrecereaRezervarilorLaClasaSuperioara(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinireaRezervarilorCuCheckinCuUnProcentaj(lista, undoList, redoList)
        elif optiune == "6":
            print(uiPretulMaximPentruFiecareClasa(lista))
        elif optiune == "7":
            print(uiOrdonareDescrescatorDupaPret(lista))
        elif optiune == "8":
            print(uiSumePreturiPerNume(lista))
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")