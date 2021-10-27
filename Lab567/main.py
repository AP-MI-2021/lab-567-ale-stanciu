from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 255, "nu", lista)
    runMenu(lista)

if __name__ == '__main__':
    main()