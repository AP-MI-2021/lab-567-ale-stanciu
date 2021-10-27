from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)


    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Stanciu Alexandra"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 200
    assert getCheckin(getById("1", lista)) == "da"

def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 200, "da", lista)

    lista = stergeRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None



    lista = stergeRezervare("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None



def testModificaRezervarea():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 200, "da", lista)

    lista = modificaRezervare("1", "Ionescu Maria", "business", 255, "nu", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ionescu Maria"
    assert getClasa(rezervareUpdatata) == "business"
    assert getPret(rezervareUpdatata) == 255
    assert getCheckin(rezervareUpdatata) == "nu"

    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "Popescu Andrei"
    assert getClasa(rezervareNeupdatata) == "economy"
    assert getPret(rezervareNeupdatata) == 200
    assert getCheckin(rezervareNeupdatata) == "da"

    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = modificaRezervare("3", "Ionescu Maria", "business", 255, "nu", lista)

    prajituraNeupdatata = getById("1", lista)
    assert getId(prajituraNeupdatata) == "1"
    assert getNume(prajituraNeupdatata) == "Stanciu Alexandra"
    assert getClasa(prajituraNeupdatata) == "economy"
    assert getPret(prajituraNeupdatata) == 200
    assert getCheckin(prajituraNeupdatata) == "da"

def testGetById():
    lista = []
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)
    lista = adaugaRezervare("5", "Popa Cristina", "business", 255, "nu", lista)

    assert getById("1", lista) is not None
    assert getById("7", lista) is None

