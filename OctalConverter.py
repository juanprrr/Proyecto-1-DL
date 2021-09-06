
class OctalConverter:
    """
        Clase OctalConverter que recibe un número octal de 4 dígitos y puede convertirlo
        a base binaria, decimal y hexadecimal. 
        Atributos: 
            data: int número a convertir; 
            count: int contador para validar la longitud del dato; 
            result: string para almacenar dato en base binaria. 
        Métodos:
            toBinary(): convierte el dato a base binaria. Retorna string result; 
            toDec(): convierte el dato a base decimal a partir de su conversión binaria. Retorna int dec; 
            toHex(): convierte el dato a base hexadecimal a partir de su conversión binaria. Retorna string result. 
    """
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.result = ""
    
    def toBinary(self):
        digits = [[0, "000"], [1, "001"], [2, "010"], [3, "011"], [4, "100"], [5, "101"], [6, "110"], [7, "111"]]
        if self.isValid(self.data):
            while self.data != 0:
                for digit in digits:
                    if digit[0] == self.data%10:
                        self.result = digit[1] + self.result
                        self.data //= 10   
            return self.result
        else:
            print("Error. Ingrese un número de 4 o menos dígitos menores a 8.")  
         

    def toDec(self):
        bin = int(self.toBinary())
        dec = 0
        exp = 0
        while bin != 0:
            dec = bin%10 * 2 **exp + dec
            exp += 1
            bin //= 10
        return str(dec)
    
    def toHex(self):
        dec = int(self.toDec())
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
        result = ""
        while dec != 0:
            result = digits[dec%16] + result
            dec //= 16
        return result

    def isValid(self, data):
        ref = data        
        while ref != 0:
            if self.count >= 4 :
                return False
            elif ref%10 > 7:
                print(ref%10)
                return False
            else:
                self.count += 1
                return self.isValid(ref//10)   
        return True
'''
test = OctalConverter(9234)
print(test.toBinary())
print(test.toDec())
print(test.toHex())
'''
