from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.command_line_console import runMENIU
from UI.console import runMenu


def Meniu():
    print("1. Interfata veche")
    print("2. Interfata noua")
    print("x. Iesire")

def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320, "da", lista)
    lista = adaugaRezervare("3", "Marinescu Raluca", "economy plus", 190, "da", lista)
    lista = adaugaRezervare("4", "Ionescu Maria", "business", 255, "nu", lista)
    lista = adaugaRezervare("5", "Pop Alexandru", "business", 300, "da", lista)
    while True:
        Meniu()
        optiune = input("Alegeti o interfata: ")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runMENIU(lista)
        elif optiune =="x":
            break
        else:
            print("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()