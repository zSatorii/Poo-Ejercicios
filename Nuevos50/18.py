import math

class Forma:
    def calcular_area(self):
        raise NotImplementedError
    
    def calcular_perimetro(self):
        raise NotImplementedError

class Poligono(Forma):
    def __init__(self, lados):
        self.lados = lados

class Triangulo(Poligono):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(3)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio