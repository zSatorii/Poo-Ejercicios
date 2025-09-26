class Calculadora:
    def __init__(self):
        self.historial = []
    
    def sumar(self, a, b):
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado
    
    def restar(self, a, b):
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado