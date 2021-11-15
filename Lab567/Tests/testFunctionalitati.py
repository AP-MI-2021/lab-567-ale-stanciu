from Domain.rezervare import getClasa, getPret, getId
from Logic.CRUD import adaugaRezervare, getByNume, getById
from Logic.functionalitati import trecereaRezervarilorLaClasaSuperioara, ieftinireaRezervarilorCuCheckinCuUnProcentaj, \
    pretulMaximPentruFiecareClasa, ordonareDescrescatorDupaPret, sumePreturiPerNume


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

def testOrdonareDescrescatorDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200.0, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320.0, "da", lista)
    lista = adaugaRezervare("3", "Ionescu Maria", "business", 255.0, "da", lista)
    lista = adaugaRezervare("4", "Marinescu Raluca", "economy plus", 275.0, "da", lista)


    rezultat = ordonareDescrescatorDupaPret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "4"
    assert getId(rezultat[2]) == "3"
    assert getId(rezultat[3]) == "1"

def testSumePreturiPerNume():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200.0, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320.0, "da", lista)
    lista = adaugaRezervare("3", "Stanciu Alexandra", "business", 255.0, "da", lista)
    lista = adaugaRezervare("4", "Marinescu Raluca", "economy plus", 275.0, "da", lista)

    rezultat = sumePreturiPerNume(lista)

    assert len(rezultat) == 3
    assert rezultat["Stanciu Alexandra"] == 455
    assert rezultat["Popescu Andrei"] == 320
    assert rezultat["Marinescu Raluca"] == 275



