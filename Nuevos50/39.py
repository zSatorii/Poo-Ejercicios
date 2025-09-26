class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin_estimada):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_estimada = fecha_fin_estimada
        self.tareas = []
        self.equipo = []
        self.estado = "planificacion"
        self.presupuesto = 0
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def calcular_progreso(self):
        if not self.tareas:
            return 0
        tareas_completadas = sum(1 for t in self.tareas if t.estado == "completada")
        return (tareas_completadas / len(self.tareas)) * 100

class Tarea:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, responsable):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.responsable = responsable
        self.estado = "pendiente"
        self.dependencias = []
        self.tiempo_estimado = 0
        self.tiempo_real = 0
    
    def puede_iniciarse(self):
        return all(dep.estado == "completada" for dep in self.dependencias)
    
    def completar(self, tiempo_real):
        if self.puede_iniciarse():
            self.estado = "completada"
            self.tiempo_real = tiempo_real
            return True
        return False

class EmpleadoProyecto:
    def __init__(self, nombre, rol, habilidades):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.rol = rol
        self.habilidades = habilidades
        self.tareas_asignadas = []
        self.disponible = True
    
    def asignar_tarea(self, tarea):
        if self.disponible:
            self.tareas_asignadas.append(tarea)
            tarea.responsable = self

class Equipo:
    def __init__(self, nombre, lider):
        self.nombre = nombre
        self.lider = lider
        self.miembros = [lider]
        self.proyectos_activos = []
    
    def agregar_miembro(self, empleado):
        if empleado not in self.miembros:
            self.miembros.append(empleado)
