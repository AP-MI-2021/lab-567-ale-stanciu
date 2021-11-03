from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from UI.console import showAll


def citesteInLinie():
    lista_mare = []
    lista_mica = []
    sir = input("Dati niste comenzi din urmatoarea lista: Adauga, Sterge, Modifica, ShowAll. "
                "Acestea trebuie sa fie separate prin '; ', iar elementele fiecareia prin ', '. "
                "Este important sa puneti un spatiu dupa caracterele ';', respectiv ',' si sa respectati numarul parametrilor fiecarei functii. ")
    lista = sir.split('; ')
    for lista_de_lista in lista:
        cuvant = lista_de_lista.split(', ')
        lista_mica = []
        for i in range(len(cuvant)):
            lista_mica.append(cuvant[i])
        lista_mare.append(lista_mica)
    return lista_mare


def UIAdaugaORezervare(lista, lista_data):
    """
    Adauga o noua rezervare in lista deja existenta
    :param lista: lista de rezervari
    :param lista_data: lista cu rezervarea data care trebuie adaugata in lista deja existenta
    :return: lista modificata
    """
    try:
        return adaugaRezervare(lista_data[0], lista_data[1], lista_data[2], float(lista_data[3]), lista_data[4], lista)
    except ValueError as ve:
        print("Eroare: ",ve)
        return lista


def UIStergeORezervare(lista, lista_data):
    """
    Sterge o rezervare din lista deja existenta
    :param lista: lista de rezrvari
    :param lista_data: lista cu rezervarea data care trebuie stearsa din lista deja existenta
    :return: lista modificata
    """
    try:
        return stergeRezervare(lista_data[0], lista)
    except ValueError as ve:
        print("Eroare: ",ve)
        return lista

def UIModificaORezervare(lista, lista_data):
    """
    Modifica o lista din lista deja existenta
    :param lista: lista de rezervari
    :param lista_data: lista cu rezervarea data care trebuie modificata in lista deja existenta
    :return: lista modificata
    """
    try:
        return adaugaRezervare(lista_data[0], lista_data[1], lista_data[2], float(lista_data[3]), lista_data[4], lista)
    except ValueError as ve:
        print("Eroare: ",ve)
        return lista

def runMENIU(lista_rezervari):
    lista_lista = citesteInLinie()
    lista_comenzi = ["Adauga", "Sterge", "Modifica", "ShowAll"]
    for lista in lista_lista:
         if lista[0] in lista_comenzi:
            if lista[0] == lista_comenzi[0]:
                lista_noua = lista[1:]
                lista_rezervari = UIAdaugaORezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[1]:
                lista_noua = lista[1:]
                lista_rezervari = UIStergeORezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[2]:
                lista_noua = lista[1:]
                lista_rezervari = UIModificaORezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[3]:
                showAll(lista_rezervari)
