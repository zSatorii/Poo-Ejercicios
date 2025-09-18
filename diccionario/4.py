class SistemaCalificaciones:
    def __init__(self, materia):
        self.materia = materia
        self.estudiantes = {}  # Diccionario: estudiante -> nota
    
    def agregar_nota(self, estudiante, nota):
        self.estudiantes[estudiante] = nota
    
    def evaluar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            nota = self.estudiantes[estudiante]
            if nota < 3.0:
                print(f"{estudiante}: {nota} - Reprobado")
            if nota >= 3.0 and nota < 4.0:
                print(f"{estudiante}: {nota} - Aprobado")
            if nota >= 4.0 and nota < 4.5:
                print(f"{estudiante}: {nota} - Bueno")
            if nota >= 4.5:
                print(f"{estudiante}: {nota} - Excelente")
        if estudiante not in self.estudiantes:
            print("Estudiante no encontrado")
    
    def reporte_general(self):
        print(f"Reporte de {self.materia}:")
        reprobados = 0
        aprobados = 0
        for estudiante, nota in self.estudiantes.items():
            if nota < 3.0:
                reprobados += 1
                print(f"{estudiante}: {nota} - REPROBADO")
            if nota >= 3.0:
                aprobados += 1
                print(f"{estudiante}: {nota} - APROBADO")
        if reprobados > 0:
            print(f"Total reprobados: {reprobados}")
        if aprobados > 0:
            print(f"Total aprobados: {aprobados}")

# Uso
sistema1 = SistemaCalificaciones("Matemáticas")
sistema1.agregar_nota("Juan", 2.5)
sistema1.agregar_nota("Ana", 4.2)
sistema1.agregar_nota("Carlos", 4.8)
sistema1.evaluar_estudiante("Ana")
sistema1.reporte_general()
