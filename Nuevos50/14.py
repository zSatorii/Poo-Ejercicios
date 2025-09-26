from datetime import datetime

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now()

class ListaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
    
    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
    
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
    
    def obtener_pendientes(self):
        return [t for t in self.tareas if not t.completada]
    
    def obtener_completadas(self):
        return [t for t in self.tareas if t.completada]
    
    def estadisticas(self):
        total = len(self.tareas)
        completadas = len(self.obtener_completadas())
        pendientes = total - completadas
        return {'total': total, 'completadas': completadas, 'pendientes': pendientes}