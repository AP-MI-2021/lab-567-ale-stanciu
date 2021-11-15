from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin
from Logic.CRUD import getByNume


def trecereaRezervarilorLaClasaSuperioara(nume, lista):
    """
    Trece toate rezervarile facute pe un nume citit la o clasa superioara
    :param nume: numele clientului pentru care trebuie modificata clasa - string
    :param lista: lista de rezervari
    :return: lista modificata
    """
    if getByNume(nume, lista) is None:
        print(ValueError("Numele nu exista!"))
        return lista
    else:
        listaNoua = []
        for rezervare in lista:
            if getNume(rezervare) == nume:
                if getClasa(rezervare) == "economy":
                    rezervareNoua = creeazaRezervare(
                        getId(rezervare),
                        getNume(rezervare),
                        "economy plus",
                        getPret(rezervare),
                        getCheckin(rezervare)
                    )
                    listaNoua.append(rezervareNoua)
                elif getClasa(rezervare) == "economy plus":
                    rezervareNoua = creeazaRezervare(
                        getId(rezervare),
                        getNume(rezervare),
                        "business",
                        getPret(rezervare),
                        getCheckin(rezervare)
                    )
                    listaNoua.append(rezervareNoua)
                elif getClasa(rezervare) == "business":
                    rezervareNoua = creeazaRezervare(
                        getId(rezervare),
                        getNume(rezervare),
                        "business",
                        getPret(rezervare),
                        getCheckin(rezervare)
                    )
                    listaNoua.append(rezervareNoua)
            else:
                listaNoua.append(rezervare)
        return listaNoua


def ieftinireaRezervarilorCuCheckinCuUnProcentaj(procent, lista):
    """
    Toate rezervarile la care s-a facut checkin vor fi ieftinite cu un procentaj citit
    :param procent: procentajul cu care se vor ieftini preturile rezervarilor - intreg
    :param lista: lista de rezervari
    :return: lista de rezervari modificata
    """
    if procent < 0 or procent > 100:
        print(ValueError("Procentul nu este corect!"))
        return lista
    else:
        lista_noua = []
        for rezervare in lista:
            if getCheckin(rezervare) == "da":
                rezervare_noua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    getClasa(rezervare),
                    getPret(rezervare) - procent / 100 * getPret(rezervare),
                    getCheckin(rezervare)
                )
                lista_noua.append(rezervare_noua)
            else:
                lista_noua.append(rezervare)
        return lista_noua



def pretulMaximPentruFiecareClasa(lista):
    """
    Determina pretul maxim pentru fiecare clasa
    :param lista: lista de rezervari
    :return: pretul maxim pentru fiecare clasa
    """
    maxim_economy = 0
    maxim_economy_plus = 0
    maxim_business = 0
    for rezervare in lista:
        if getClasa(rezervare) == "economy":
            if getPret(rezervare) > maxim_economy:
                maxim_economy = getPret(rezervare)
        elif getClasa(rezervare) == "economy plus":
            if getPret(rezervare) > maxim_economy_plus:
                maxim_economy_plus = getPret(rezervare)
        elif getClasa(rezervare) == "business":
            if getPret(rezervare) > maxim_business:
                maxim_business = getPret(rezervare)
    return "maxim economy: {}, maxim economy: {}, maxim business: {}".format(
        maxim_economy,
        maxim_economy_plus,
        maxim_business
    )

def ordonareDescrescatorDupaPret(lista):
    """
    Ordoneaza rezervarile descrescator dupa pret
    :param lista: lista de rezervari
    :return: lista de rezervari ordonata
    """
    return sorted(lista, reverse=True, key=lambda rezervare: getPret(rezervare))

def sumePreturiPerNume(lista):
    """
    Afiseaza suma preturilor pentru fiecare nume
    :param lista: lista de rezervari
    :return: suma preturilor pentru fiecare nume
    """
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] += pret
        else:
            rezultat[nume] = pret
    return rezultat
