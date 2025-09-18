class Color:
    def __init__(self, nombre):
        self.nombre = nombre

colores = ["rojo", "azul", "verde"]

c1 = Color(colores)
c2 = Color(colores[1])
c3 = Color(colores)

if c1.nombre == "azul":
    print("¿El color de c1 es azul? VERDADERO")
else:
    print("¿El color de c1 es azul? FALSO")

if c2.nombre == "azul":
    print("¿El color de c2 es azul? VERDADERO")
else:
    print("¿El color de c2 es azul? FALSO")

if c3.nombre == "azul":
    print("¿El color de c3 es azul? VERDADERO")
else:
    print("¿El color de c3 es azul? FALSO")
