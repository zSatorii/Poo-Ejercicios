import random

class Personaje:
    def __init__(self, nombre, clase="Guerrero"):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self.vida = 100
        self.vida_maxima = 100
        self.mana = 50
        self.mana_maximo = 50
        self.experiencia = 0
        self.inventario = []
        self._configurar_clase()
    
    def _configurar_clase(self):
        configs = {
            "Guerrero": {"vida": 120, "mana": 30, "ataque": 15},
            "Mago": {"vida": 80, "mana": 100, "ataque": 10},
            "Arquero": {"vida": 90, "mana": 60, "ataque": 12}
        }
        if self.clase in configs:
            config = configs[self.clase]
            self.vida = self.vida_maxima = config["vida"]
            self.mana = self.mana_maximo = config["mana"]
            self.ataque = config["ataque"]
    
    def atacar(self, objetivo):
        if self.vida <= 0:
            return f"{self.nombre} está muerto"
        
        daño = self.ataque + random.randint(1, 6)
        objetivo.recibir_daño(daño)
        return f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño"
    
    def recibir_daño(self, cantidad):
        self.vida = max(0, self.vida - cantidad)
    
    def ganar_experiencia(self, exp):
        self.experiencia += exp
        if self.experiencia >= self.nivel * 100:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.vida_maxima += 20
        self.vida = self.vida_maxima
        self.mana_maximo += 10
        self.mana = self.mana_maximo
        self.experiencia = 0

class Item:
    def __init__(self, nombre, tipo, valor=0):
        self.nombre = nombre
        self.tipo = tipo  # arma, armadura, poción
        self.valor = valor
    
    def usar(self, personaje):
        if self.tipo == "poción":
            personaje.vida = min(personaje.vida_maxima, personaje.vida + self.valor)
            return f"{personaje.nombre} usa {self.nombre} y recupera {self.valor} vida"
        return f"{self.nombre} no se puede usar"
