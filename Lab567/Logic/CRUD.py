from Domain.rezervare import creeazaRezervare, getId, getNume


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    adauga o rezervare intr-o lista
    :param id: id-ul de adaugat - string
    :param nume: numele de adaugat - string
    :param clasa: clasa de adaugat - string
    :param pret: pretul de adaugat - float
    :param checkin: checkin-ul de adaugat - string
    :param lista: lista noua
    :return: o lista continand lista veche + o noua rezervare
    """
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def getById(id, lista):
    """
    ia rezervarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat sau None, daca nu exista nicio rezervare cu id-ul dat
    """
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def getByNume(nume, lista):
    """
    ia rezervarea cu numele dat dintr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea cu numele dat sau None, daca nu exista nicio rezervare cu numele dat
    """
    for rezervare in lista:
        if getNume(rezervare) == nume:
            return rezervare
    return None

def stergeRezervare(id, lista):
    """
    sterge o rezervare dintr-o lista dupa id
    :param id: string
    :param lista: lista de rezervari
    :return: lista de rezervari
    """
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    """

    :param id: id-ul dupa care se face modificarea
    :param nume: noul nume
    :param clasa: noua clasa
    :param pret: noul pret
    :param checkin: noul checkin
    :param lista: noua lista
    :return:
    """
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua