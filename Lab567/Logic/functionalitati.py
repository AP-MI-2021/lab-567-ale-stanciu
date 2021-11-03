from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin


def trecereaRezervarilorLaClasaSuperioara(nume, lista):
    """
    Trece toate rezervarile facute pe un nume citit la o clasa superioara
    :param nume: numele clientului pentru care trebuie modificata clasa - string
    :param lista: lista de rezervari
    :return: lista modificata
    """
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
    maxim_economy = -1
    maxim_economy_plus = -1
    maxim_business = -1
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