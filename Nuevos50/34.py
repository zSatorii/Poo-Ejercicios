class EstudianteMusica:
    def __init__(self, nombre, instrumento_principal):
        self.nombre = nombre
        self.instrumento_principal = instrumento_principal
        self.nivel = "principiante"
        self.clases_tomadas = []
        self.progreso = {}
    
    def actualizar_progreso(self, habilidad, puntuacion):
        self.progreso[habilidad] = puntuacion
        
        # Determinar nivel basado en progreso
        promedio = sum(self.progreso.values()) / len(self.progreso) if self.progreso else 0
        if promedio >= 80:
            self.nivel = "avanzado"
        elif promedio >= 60:
            self.nivel = "intermedio"

class ProfesorMusica:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.estudiantes = []
        self.horarios = {}
    
    def evaluar_estudiante(self, estudiante, habilidad, puntuacion):
        estudiante.actualizar_progreso(habilidad, puntuacion)
        return f"{estudiante.nombre} evaluado en {habilidad}: {puntuacion}/100"

class ClaseMusica:
    def __init__(self, tipo, profesor, duracion=60):
        self.tipo = tipo  # individual, grupal
        self.profesor = profesor
        self.duracion = duracion  # minutos
        self.estudiantes = []
        self.fecha = None
    
    def agregar_estudiante(self, estudiante):
        if self.tipo == "individual" and len(self.estudiantes) == 0:
            self.estudiantes.append(estudiante)
            estudiante.clases_tomadas.append(self)
        elif self.tipo == "grupal" and len(self.estudiantes) < 6:
            self.estudiantes.append(estudiante)
            estudiante.clases_tomadas.append(self)

class EscuelaMusica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}
        self.profesores = {}
        self.clases = []
        self.instrumentos_disponibles = ["piano", "guitarra", "violín", "batería", "flauta"]
    
    def matricular_estudiante(self, estudiante):
        self.estudiantes[estudiante.nombre] = estudiante
    
    def programar_recital(self, fecha, participantes):
        return {
            'fecha': fecha,
            'participantes': participantes,
            'tipo': 'recital',
            'estado': 'programado'
        }