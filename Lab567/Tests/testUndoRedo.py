from Logic.CRUD import adaugaRezervare, getById
from UI.console import undoTestare, redoTestare


def testUndoRedo():
    lista  = []
    undoList = []
    redoList = []

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("3", "Marinescu Raluca", "economy plus", 190, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("4", "Ionescu Maria", "business", 255, "nu", lista)

    assert len(lista) == 4

    lista = undoTestare(lista, undoList, redoList)

    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("4", lista) is None

    lista = undoTestare(lista, undoList, redoList)
    lista = undoTestare(lista, undoList, redoList)
    lista = undoTestare(lista, undoList, redoList)

    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("4", lista) is None

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("1", "Stanciu Alexandra", "economy", 200, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("2", "Popescu Andrei", "economy", 320, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("3", "Marinescu Raluca", "economy plus", 190, "da", lista)

    undoList.append(lista)
    redoList.clear()
    lista = adaugaRezervare("4", "Ionescu Maria", "business", 255, "nu", lista)

    lista = undoTestare(lista, undoList, redoList)

    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None
    assert getById("4", lista) is None

    lista = redoTestare(lista, undoList, redoList)

    assert len(lista) == 4
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None
    assert getById("4", lista) is not None

    lista = undoTestare(lista, undoList, redoList)
    lista = undoTestare(lista, undoList, redoList)
    lista = undoTestare(lista, undoList, redoList)

    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    lista = redoTestare(lista, undoList, redoList)
    lista = redoTestare(lista, undoList, redoList)

    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None
    assert getById("4", lista) is None




