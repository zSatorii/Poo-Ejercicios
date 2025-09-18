class alumno:
    def __init__(self, nombre, documento, edad, ficha, programa):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad
        self.ficha = ficha
        self.programa = programa
alumno1 = alumno("Johan", "1019020634", "19 años", "3203084", "Analisis y desarrollo de sistemas de informacion")
print(alumno1.nombre, alumno1.documento, alumno1.edad, alumno1.ficha, alumno1.programa)
        