class sena:
    def __init__(self, nombre, sede, programa, ficha, jornada):
        self.nombre = nombre
        self.sede = sede
        self.programa = programa
        self.ficha = ficha
        self.jornada = jornada
sena1 = sena("Johan", "Sede centro", "Analisis y desarrollo de sistemas de informacion", "3203084", "Diurna")
print(sena1.nombre, sena1.sede, sena1.programa, sena1.ficha, sena1.jornada)
