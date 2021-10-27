from Domain.rezervare import getClasa
from Logic.CRUD import adaugaRezervare, getByNume
from Logic.functionalitati import trecereaRezervarilorLaClasaSuperioara


def testTrecereaRezervarilorLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 255, "nu", lista)

    lista = trecereaRezervarilorLaClasaSuperioara("Stanciu Alexandra", lista)

    assert getClasa(getByNume("Stanciu Alexandra", lista)) == "economy plus"
    assert getClasa(getByNume("Ionescu Maria", lista)) == "business"