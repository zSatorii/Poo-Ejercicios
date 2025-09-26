import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def __eq__(self, otra):
        return self.valor == otra.valor

class Baraja:
    def __init__(self):
        palos = ["Corazones", "Diamantes", "Tréboles", "Espadas"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cartas = [Carta(palo, valor) for palo in palos for valor in valores]
    
    def mezclar(self):
        random.shuffle(self.cartas)
    
    def repartir_carta(self):
        return self.cartas.pop() if self.cartas else None

class Mano:
    def __init__(self):
        self.cartas = []
    
    def recibir_carta(self, carta):
        self.cartas.append(carta)
    
    def mostrar_mano(self):
        return [str(carta) for carta in self.cartas]
