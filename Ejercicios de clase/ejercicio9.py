class granja:
    def __init__(self, nombre, ubicacion, tamano, animales):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tamano = tamano
        self.animales = animales
granja1 = granja("Granja todoterreno", "Zona Rural", "100 hectareas", "Vacas, cerdos, gallinas")
print(granja1.nombre, granja1.ubicacion, granja1.tamano, granja1.animales)
        