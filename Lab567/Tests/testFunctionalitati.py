from Domain.rezervare import getClasa, getPret
from Logic.CRUD import adaugaRezervare, getByNume, getById
from Logic.functionalitati import trecereaRezervarilorLaClasaSuperioara, ieftinireaRezervarilorCuCheckinCuUnProcentaj, \
    pretulMaximPentruFiecareClasa


def testTrecereaRezervarilorLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 255, "nu", lista)

    lista = trecereaRezervarilorLaClasaSuperioara("Stanciu Alexandra", lista)

    assert getClasa(getByNume("Stanciu Alexandra", lista)) == "economy plus"
    assert getClasa(getByNume("Ionescu Maria", lista)) == "business"

def testIeftinireaRezervarilorCuCheckinCuUnProcentaj():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 300, "nu", lista)

    lista = ieftinireaRezervarilorCuCheckinCuUnProcentaj(10, lista)

    assert getPret(getById("1", lista)) == 180

def testPretulMaximPentruFiecareClasa():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200.0, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320.0, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 255.0, "da", lista)
    lista = adaugaRezervare("4", "Marinescu Raluca", "economy plus", 255.0, "da", lista)


    lista = pretulMaximPentruFiecareClasa(lista) == "maxim economy: 320.0, maxim economy plus: 255.0, maxim business: 255.0"
