from math import *

tabla_hamming = []

def binarioHamming(binario):
    p = 1
    n = 0
    contUnos = 0
    paridad = []


def hileraHamming(binario):
    n = 1;
    cont = 0;
    hilerahamming = ""
    while cont < len(binario):
        if potenciaDos(n):
            hilerahamming = hilerahamming + "p"
        else:
            hilerahamming = hilerahamming + binario[cont]
            cont = cont + 1
        n = n + 1
    return hilerahamming

def calcParidad(hamming, paridad):
    n = 0
    pos = (2 ** n) - 1
    eval = 0
    cont_unos = 0
    hileraParidad = ""
    while 2**n < len(hamming):
        cont_unos = 0
        while pos < len(hamming):
            if eval >= 2**n:
                eval = 0
                pos = pos + 2**n
            elif hamming[pos] == "0":
               pos = pos + 1
               eval = eval + 1
            elif hamming[pos] == "p":
               pos = pos + 1
               eval = eval + 1
            elif hamming[pos] == "1":
               pos = pos + 1
               eval = eval + 1
               cont_unos = cont_unos + 1
        if cont_unos % 2 == 0:
            if paridad == "par":
                hileraParidad = reemplazar(hamming, 2**n - 1, "0")
                hamming = hileraParidad
            elif paridad == "impar":
                hileraParidad = reemplazar(hamming, 2**n - 1, "1")
                hamming = hileraParidad
        elif cont_unos % 2 != 0:
            if paridad == "par":
                hileraParidad = reemplazar(hamming, 2**n - 1, "1")
                hamming = hileraParidad
            elif paridad == "impar":
                hileraParidad = reemplazar(hamming, 2**n - 1, "0")
                hamming = hileraParidad
        n = n + 1
        pos = 2 ** n - 1
        cont_unos = 0
        eval = 0
    print(hileraParidad)
    return hileraParidad

def comprobar(hamming, paridad):
    global tabla_hamming
    n = 0
    pos = (2 ** n) - 1
    eval = 0
    error = False
    cont_unos = 0
    calc_paridades = ""
    while 2 ** n < len(hamming):
        cont_unos = 0
        while pos < len(hamming):
            if eval >= 2 ** n:
                eval = 0
                pos = pos + 2 ** n
            elif hamming[pos] == "0":
                pos = pos + 1
                eval = eval + 1
            elif hamming[pos] == "1":
                pos = pos + 1
                eval = eval + 1
                cont_unos = cont_unos + 1
        if cont_unos % 2 == 0:
            if paridad == "par":
                calc_paridades = calc_paridades + "0"
            elif paridad == "impar":
                calc_paridades = calc_paridades + "1"
                error = True
        elif cont_unos % 2 != 0:
            if paridad == "par":
                calc_paridades = calc_paridades + "1"
                error = True
            elif paridad == "impar":
                calc_paridades = calc_paridades + "0"
        n = n + 1
        pos = 2 ** n - 1
        cont_unos = 0
        eval = 0
    print(calc_paridades)
    return calc_paridades


def reemplazar(hilera, pos, valor):
    nuevaHilera = ""
    i = 0
    while i < len(hilera):
        if i  == pos:
            nuevaHilera = nuevaHilera + valor
        else:
            nuevaHilera = nuevaHilera + hilera[i]
        i = i + 1
    return nuevaHilera

def potenciaDos(valor):
    cont = 0
    while cont < 20:
        if valor == 2**cont:
            return True
        cont = cont + 1
    return False


calcParidad(hileraHamming("111011101100"),"impar")
comprobar("00111100111011010","impar")
