class Vehiculo:
    def __init__(self, id_vehiculo, tipo, capacidad):
        self.id_vehiculo = id_vehiculo
        self.tipo = tipo  # bus, metro, taxi
        self.capacidad = capacidad
        self.pasajeros_actuales = 0
        self.en_servicio = True

class Ruta:
    def __init__(self, nombre, estaciones, tiempo_total):
        self.nombre = nombre
        self.estaciones = estaciones
        self.tiempo_total = tiempo_total  # en minutos
        self.vehiculos_asignados = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos_asignados.append(vehiculo)
    
    def tiempo_entre_estaciones(self, estacion_origen, estacion_destino):
        try:
            indice_origen = self.estaciones.index(estacion_origen)
            indice_destino = self.estaciones.index(estacion_destino)
            distancia = abs(indice_destino - indice_origen)
            return (distancia / (len(self.estaciones) - 1)) * self.tiempo_total
        except ValueError:
            return None

class Pasajero:
    def __init__(self, nombre, id_pasajero):
        self.nombre = nombre
        self.id_pasajero = id_pasajero
        self.viajes = []
    
    def planear_viaje(self, estacion_origen, estacion_destino, ruta):
        tiempo = ruta.tiempo_entre_estaciones(estacion_origen, estacion_destino)
        if tiempo:
            viaje = {
                'origen': estacion_origen,
                'destino': estacion_destino,
                'ruta': ruta.nombre,
                'tiempo_estimado': tiempo
            }
            self.viajes.append(viaje)
            return viaje
        return None

class SistemaTransporte:
    def __init__(self):
        self.rutas = {}
        self.vehiculos = {}
        self.pasajeros = {}
    
    def agregar_ruta(self, ruta):
        self.rutas[ruta.nombre] = ruta
    
    def buscar_ruta_optima(self, origen, destino):
        rutas_posibles = []
        for ruta in self.rutas.values():
            if origen in ruta.estaciones and destino in ruta.estaciones:
                tiempo = ruta.tiempo_entre_estaciones(origen, destino)
                rutas_posibles.append((ruta, tiempo))
        
        if rutas_posibles:
            return min(rutas_posibles, key=lambda x: x[1])
        return None