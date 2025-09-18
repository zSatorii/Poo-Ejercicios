class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.notas = {} 
    
    def agregar_nota(self, materia, nota):
        self.notas[materia] = nota
    
    def obtener_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
    def mostrar_info(self):
        promedio = self.obtener_promedio()
        print(f"Estudiante: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {promedio:.2f}")

estudiante1 = Estudiante("Carlos", 16, "10°")
estudiante1.agregar_nota("Matemáticas", 4.5)
estudiante1.agregar_nota("Español", 4.0)
estudiante1.agregar_nota("Ciencias", 4.8)
estudiante1.mostrar_info()
