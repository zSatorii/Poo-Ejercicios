class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.calificaciones = {}
    
    def agregar_calificacion(self, materia, nota):
        self.calificaciones[materia.nombre] = {'materia': materia, 'nota': nota}
    
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        
        suma_ponderada = sum(
            cal['nota'] * cal['materia'].creditos 
            for cal in self.calificaciones.values()
        )
        total_creditos = sum(
            cal['materia'].creditos 
            for cal in self.calificaciones.values()
        )
        
        return suma_ponderada / total_creditos if total_creditos > 0 else 0

class SistemaCalificaciones:
    def __init__(self):
        self.estudiantes = {}
        self.materias = {}
    
    def registrar_estudiante(self, estudiante):
        self.estudiantes[estudiante.id_estudiante] = estudiante
    
    def registrar_materia(self, materia):
        self.materias[materia.nombre] = materia
    
    def generar_reporte_estudiante(self, id_estudiante):
        if id_estudiante in self.estudiantes:
            est = self.estudiantes[id_estudiante]
            return {
                'nombre': est.nombre,
                'calificaciones': est.calificaciones,
                'promedio': est.calcular_promedio()
            }
        return None