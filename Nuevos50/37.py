class Hotel:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = {}
        self.servicios = []
        self.reservas = []

class Habitacion:
    def __init__(self, numero, tipo, precio_noche, capacidad):
        self.numero = numero
        self.tipo = tipo  # simple, doble, suite
        self.precio_noche = precio_noche
        self.capacidad = capacidad
        self.servicios = []
        self.disponible = True
    
    def esta_disponible(self, fecha_entrada, fecha_salida):
        # Verificar si hay reservas que se superpongan
        return self.disponible

class Huesped:
    def __init__(self, nombre, documento, email, telefono):
        self.nombre = nombre
        self.documento = documento
        self.email = email
        self.telefono = telefono
        self.historial_reservas = []

class ReservaHotel:
    def __init__(self, huesped, habitacion, fecha_entrada, fecha_salida):
        self.id = str(uuid.uuid4())
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = "confirmada"
        self.servicios_adicionales = []
        self.total = self.calcular_total()
    
    def calcular_total(self):
        noches = (self.fecha_salida - self.fecha_entrada).days
        total_habitacion = noches * self.habitacion.precio_noche
        total_servicios = sum(s['precio'] for s in self.servicios_adicionales)
        return total_habitacion + total_servicios
    
    def check_in(self):
        self.estado = "check_in"
        self.habitacion.disponible = False
    
    def check_out(self):
        self.estado = "check_out"
        self.habitacion.disponible = True
