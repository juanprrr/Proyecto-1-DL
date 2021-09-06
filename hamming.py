from math import *


class Hamming:
    def __init__(self):
        self.hileraParidad = None
        self.tabla_hamming = []
        self.tabla_paridad = []
        self.paridades = None
        self.hilerahamming = ""

    def binarioHamming(self, binario):
        p = 1
        n = 0
        contUnos = 0
        paridad = []


    def hileraHamming(self, binario):
        n = 1
        cont = 0
        hilerahamming = ""
        while cont < len(binario):
            if self.potenciaDos(n):
                hilerahamming = hilerahamming + "p"
            else:
                hilerahamming = hilerahamming + binario[cont]
                cont = cont + 1
            n = n + 1
        self.hilerahamming = hilerahamming
        return hilerahamming

    def calcParidad(self, hamming, paridad):
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
                    hileraParidad = self.reemplazar(hamming, 2**n - 1, "0")
                    hamming = hileraParidad
                elif paridad == "impar":
                    hileraParidad = self.reemplazar(hamming, 2**n - 1, "1")
                    hamming = hileraParidad
            elif cont_unos % 2 != 0:
                if paridad == "par":
                    hileraParidad = self.reemplazar(hamming, 2**n - 1, "1")
                    hamming = hileraParidad
                elif paridad == "impar":
                    hileraParidad = self.reemplazar(hamming, 2**n - 1, "0")
                    hamming = hileraParidad
            
            n = n + 1
            pos = 2 ** n - 1
            cont_unos = 0
            eval = 0
        self.hileraParidad = hileraParidad
        print(hileraParidad)
        return hileraParidad

    def comprobar(self, hamming, paridad):
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
                    cont = 0
                    while cont < 2 ** n:
                        self.tabla_paridad.append("_")
                        cont = cont + 1
                elif hamming[pos] == "0":
                    pos = pos + 1
                    eval = eval + 1
                    self.tabla_paridad.append("0")
                elif hamming[pos] == "1":
                    pos = pos + 1
                    eval = eval + 1
                    cont_unos = cont_unos + 1
                    self.tabla_paridad.append("1")
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
            self.tabla_hamming.append(self.tabla_paridad)
            self.tabla_paridad = []
        print(calc_paridades)
        self.paridades = calc_paridades
        print(self.tabla_hamming)
        return calc_paridades


    def reemplazar(self, hilera, pos, valor):
        nuevaHilera = ""
        i = 0
        while i < len(hilera):
            if i  == pos:
                nuevaHilera = nuevaHilera + valor
            else:
                nuevaHilera = nuevaHilera + hilera[i]
            i = i + 1
        return nuevaHilera

    def potenciaDos(self, valor):
        cont = 0
        while cont < 20:
            if valor == 2**cont:
                return True
            cont = cont + 1
        return False
    
    def toDec(self):
        bin = int(self.paridades[::-1])
        dec = 0
        exp = 0
        while bin != 0:
            dec = bin%10 * 2 **exp + dec
            exp += 1
            bin //= 10
        return str(dec)
'''
a = Hamming()
a.calcParidad(a.hileraHamming("111011101100"),"impar")
a.comprobar("00111100111011000","impar")
a.comprobar("00111100111011111","impar")
'''