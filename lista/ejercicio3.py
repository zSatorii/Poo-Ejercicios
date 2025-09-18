class sena:
    def __init__(self, nombre, apellido, edad, sede, programa):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sede = sede
        self.programa = programa
lista_aprendices = [
    ('juan', 'perez', 20, 'bucaramanga', 'python'),
    ('maria', 'lopez', 22, 'medellin', 'java'),
    ('carlos', 'garcia', 21, 'bogota', 'javascript')
]
for sena in lista_aprendices:
    print("Nombre:", sena[0], "apellido: ", sena[1], "edad: ", sena[2], "sede: ", sena[3], "programa: ", sena[4])