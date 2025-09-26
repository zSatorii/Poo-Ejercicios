from datetime import datetime, timedelta

class Recurso:
    def __init__(self, nombre, tipo, capacidad=1):
        self.nombre = nombre
        self.tipo = tipo  # sala, equipo, servicio
        self.capacidad = capacidad
        self.reservas = []
    
    def esta_disponible(self, fecha_inicio, fecha_fin):
        for reserva in self.reservas:
            if not (fecha_fin <= reserva.fecha_inicio or fecha_inicio >= reserva.fecha_fin):
                return False
        return True

class Reserva:
    def __init__(self, recurso, usuario, fecha_inicio, fecha_fin):
        self.recurso = recurso
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "activa"
        self.fecha_creacion = datetime.now()
    
    def cancelar(self):
        self.estado = "cancelada"
        self.recurso.reservas.remove(self)

class SistemaReservas:
    def __init__(self):
        self.recursos = {}
        self.usuarios = {}
        self.reservas = []
    
    def crear_reserva(self, nombre_recurso, nombre_usuario, fecha_inicio, fecha_fin):
        if nombre_recurso in self.recursos:
            recurso = self.recursos[nombre_recurso]
            if recurso.esta_disponible(fecha_inicio, fecha_fin):
                reserva = Reserva(recurso, nombre_usuario, fecha_inicio, fecha_fin)
                recurso.reservas.append(reserva)
                self.reservas.append(reserva)
                return reserva
        return None
