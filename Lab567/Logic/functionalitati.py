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