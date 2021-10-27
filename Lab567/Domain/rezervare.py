def creeazaRezervare(id, nume, clasa, pret, checkin):
    """
    creeaza un dictionar ce retine o rezervare
    :param id: id-ul rezervarii - string
    :param nume: numele clientului - string
    :param clasa: clasa de confort - string
    :param preț: pretul biletului - float
    :param checkin: checkin facut - string
    :return: un dictionar ce retine o rezervare
    """
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getId(rezervare):
    """
    da id-ul unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return:  id-ul rezervarii - string
    """
    return rezervare["id"]

def getNume(rezervare):
    """
    da numele clientului
    :param rezervare: un dictionar de tip rezervare
    :return: numele clientului - string
    """
    return rezervare["nume"]

def getClasa(rezervare):
    """
    da clasa de confort
    :param rezervare: un dictionar de tip rezervare
    :return: clasa - string
    """
    return rezervare["clasa"]

def getPret(rezervare):
    """
    da pretul rezervarii
    :param rezervare: un dictionar de tip rezervare
    :return: pretul - float
    """
    return rezervare["pret"]

def getCheckin(rezervare):
    """
    da statusul checkin-ului rezervarii
    :param rezervare: un dictionar de tip rezervare
    :return: statusul checkin-ului - string
    """
    return rezervare["checkin"]

def toString(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )



