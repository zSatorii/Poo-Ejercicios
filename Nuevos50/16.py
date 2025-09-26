class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False
    
    def acelerar(self, incremento=10):
        if self.encendido:
            self.velocidad += incremento
    
    def frenar(self, decremento=10):
        self.velocidad = max(0, self.velocidad - decremento)

class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
        self.aire_acondicionado = False
    
    def activar_aire(self):
        self.aire_acondicionado = not self.aire_acondicionado

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
    
    def acelerar(self, incremento=15):
        super().acelerar(incremento)

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, cambios):
        super().__init__(marca, modelo, 2023)
        self.cambios = cambios
        self.encendido = True  # Siempre "encendida"
    
    def acelerar(self, incremento=5):
        self.velocidad += incremento
