import random
import string

class GeneradorPassword:
    def __init__(self):
        self.mayusculas = string.ascii_uppercase
        self.minusculas = string.ascii_lowercase
        self.numeros = string.digits
        self.simbolos = "!@#$%^&*"
    
    def generar(self, longitud=8, incluir_mayus=True, incluir_minus=True, incluir_nums=True, incluir_simbolos=False):
        caracteres = ""
        if incluir_mayus:
            caracteres += self.mayusculas
        if incluir_minus:
            caracteres += self.minusculas
        if incluir_nums:
            caracteres += self.numeros
        if incluir_simbolos:
            caracteres += self.simbolos
        
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    
    def validar_fortaleza(self, password):
        puntos = 0
        if any(c.isupper() for c in password):
            puntos += 1
        if any(c.islower() for c in password):
            puntos += 1
        if any(c.isdigit() for c in password):
            puntos += 1
        if len(password) >= 8:
            puntos += 1
        
        if puntos >= 3:
            return "Fuerte"
        elif puntos >= 2:
            return "Media"
        else:
            return "Débil"