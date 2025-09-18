class Fruta:
    def __init__(self, nombre):
        self.nombre = nombre
fruta1 = Fruta("manzana")
fruta2 = Fruta("pera")

if fruta1.nombre == "manzana":
    print("¿La fruta1 es manzana? VERDADERO")
else:
    print("¿La fruta1 es manzana? FALSO")

if fruta2.nombre == "manzana":
    print("¿La fruta2 es manzana? VERDADERO")
else:
    print("¿La fruta2 es manzana? FALSO")