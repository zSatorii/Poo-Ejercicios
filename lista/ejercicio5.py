class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
datos = [
    ("Pedro", 22),
    ("Ana", 18),
    ("Luis", 31),
    ("Marta", 25)
]
personas = [Persona(nombre, edad) for nombre, edad in datos]
print(personas[0].nombre, "tiene", personas[0].edad, "años")
print(personas[1].nombre, "tiene", personas[1].edad, "años")
print(personas[2].nombre, "tiene", personas[2].edad, "años")
print(personas[3].nombre, "tiene", personas[3].edad, "años")