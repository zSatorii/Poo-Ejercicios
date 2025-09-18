class carro:
    def __init__(self, nombre):
        self.nombre = nombre
Carro1 = carro("Mazda")
Carro2 = carro("Nissan")

if Carro1.nombre == "Mazda":
    print("El carro1 es un madza? VERDADERO")
else:
    print("El carro2 es un mazda? FALSO")

if Carro2.nombre == "Nissan":
    print("El carro1 es un Nissan? VERDADERO")
else:
    print("El carro2 es un mazda? FALSO")