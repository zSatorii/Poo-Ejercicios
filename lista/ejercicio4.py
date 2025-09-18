class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

numeros = [3, 4]
calc1 = Calculadora(*numeros)
print("Suma 1:", calc1.a, "+", calc1.b, "=", calc1.sumar())