class Paquete:
    def __init__(self, remitente, destinatario, contenido, peso, dimensiones):
        self.id = str(uuid.uuid4())
        self.codigo_seguimiento = f"PKG{random.randint(100000, 999999)}"
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.peso = peso  # en kg
        self.dimensiones = dimensiones  # {"largo": x, "ancho": y, "alto": z}
        self.estado = "recibido"
        self.historial_estados = []
        self.fecha_creacion = datetime.now()
        self.prioridad = "normal"  # express, normal, economico
    
    def actualizar_estado(self, nuevo_estado, ubicacion=None):
        self.estado = nuevo_estado
        entrada_historial = {
            'estado': nuevo_estado,
            'fecha': datetime.now(),
            'ubicacion': ubicacion
        }
        self.historial_estados.append(entrada_historial)
    
    def calcular_volumen(self):
        return self.dimensiones["largo"] * self.dimensiones["ancho"] * self.dimensiones["alto"]

class VehiculoLogistica:
    def __init__(self, tipo, capacidad_peso, capacidad_volumen, conductor):
        self.id = str(uuid.uuid4())
        self.tipo = tipo  # camion, furgoneta, motocicleta
        self.capacidad_peso = capacidad_peso
        self.capacidad_volumen = capacidad_volumen
        self.conductor = conductor
        self.ubicacion_actual = {"lat": 0, "lon": 0}
        self.carga_actual = []
        self.disponible = True
        self.rutas_asignadas = []
    
    def puede_cargar(self, paquete):
        peso_actual = sum(p.peso for p in self.carga_actual)
        volumen_actual = sum(p.calcular_volumen() for p in self.carga_actual)
        
        return (peso_actual + paquete.peso <= self.capacidad_peso and
                volumen_actual + paquete.calcular_volumen() <= self.capacidad_volumen)
    
    def cargar_paquete(self, paquete):
        if self.puede_cargar(paquete):
            self.carga_actual.append(paquete)
            paquete.actualizar_estado("en_transito")
            return True
        return False

class RutaEntrega:
    def __init__(self, vehiculo, destinos):
        self.id = str(uuid.uuid4())
        self.vehiculo = vehiculo
        self.destinos = destinos  # Lista de direcciones/coordenadas
        self.distancia_total = 0
        self.tiempo_estimado = 0
        self.estado = "planificada"
        self.paquetes_asignados = []
    
    def optimizar_ruta(self):
        # Implementación simplificada del problema del vendedor viajero
        # En la práctica se usarían APIs como Google Maps o algoritmos más sofisticados
        destinos_optimizados = self.algoritmo_vecino_mas_cercano(self.destinos)
        self.destinos = destinos_optimizados
        self.calcular_distancia_tiempo()
    
    def algoritmo_vecino_mas_cercano(self, destinos):
        if len(destinos) <= 1:
            return destinos
        
        ruta_optimizada = [destinos[0]]
        destinos_restantes = destinos[1:]
        
        while destinos_restantes:
            ultimo_destino = ruta_optimizada[-1]
            destino_mas_cercano = min(destinos_restantes, 
                                    key=lambda d: self.calcular_distancia(ultimo_destino, d))
            ruta_optimizada.append(destino_mas_cercano)
            destinos_restantes.remove(destino_mas_cercano)
        
        return ruta_optimizada
    
    def calcular_distancia(self, destino1, destino2):
        # Fórmula de distancia euclidiana simplificada
        return ((destino1["lat"] - destino2["lat"]) ** 2 + 
                (destino1["lon"] - destino2["lon"]) ** 2) ** 0.5
    
    def calcular_distancia_tiempo(self):
        distancia_total = 0
        for i in range(len(self.destinos) - 1):
            distancia_total += self.calcular_distancia(self.destinos[i], self.destinos[i+1])
        
        self.distancia_total = distancia_total
        self.tiempo_estimado = distancia_total * 2  # Asumiendo 2 minutos por unidad de distancia

class AlmacenLogistica:
    def __init__(self, nombre, ubicacion, capacidad):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.paquetes_almacenados = []
        self.trabajadores = []
        self.zonas_almacenamiento = {}
    
    def recibir_paquete(self, paquete):
        if len(self.paquetes_almacenados) < self.capacidad:
            self.paquetes_almacenados.append(paquete)
            paquete.actualizar_estado("en_almacen", self.nombre)
            return True
        return False
    
    def despachar_paquete(self, paquete_id):
        paquete = next((p for p in self.paquetes_almacenados if p.id == paquete_id), None)
        if paquete:
            self.paquetes_almacenados.remove(paquete)
            paquete.actualizar_estado("despachado", self.nombre)
            return paquete
        return None

class SistemaLogistica:
    def __init__(self):
        self.paquetes = {}
        self.vehiculos = {}
        self.almacenes = {}
        self.rutas_activas = []
        self.metricas_rendimiento = {}
    
    def planificar_entregas(self, fecha):
        # Algoritmo para agrupar paquetes por región y asignar vehículos
        paquetes_pendientes = [p for p in self.paquetes.values() if p.estado == "en_almacen"]
        
        # Agrupar por región (simplificado)
        grupos_regionales = {}
        for paquete in paquetes_pendientes:
            region = f"{paquete.destinatario['ciudad']}"
            if region not in grupos_regionales:
                grupos_regionales[region] = []
            grupos_regionales[region].append(paquete)
        
        # Asignar vehículos a cada grupo
        rutas_creadas = []
        for region, paquetes in grupos_regionales.items():
            vehiculo_disponible = next((v for v in self.vehiculos.values() if v.disponible), None)
            if vehiculo_disponible:
                destinos = [{"lat": p.destinatario.get("lat", 0), 
                           "lon": p.destinatario.get("lon", 0)} for p in paquetes]
                
                ruta = RutaEntrega(vehiculo_disponible, destinos)
                ruta.paquetes_asignados = paquetes
                ruta.optimizar_ruta()
                
                vehiculo_disponible.disponible = False
                self.rutas_activas.append(ruta)
                rutas_creadas.append(ruta)
        
        return rutas_creadas
    
    def rastrear_paquete(self, codigo_seguimiento):
        paquete = next((p for p in self.paquetes.values() 
                       if p.codigo_seguimiento == codigo_seguimiento), None)
        if paquete:
            return {
                'codigo': paquete.codigo_seguimiento,
                'estado_actual': paquete.estado,
                'historial': paquete.historial_estados,
                'ubicacion_estimada': self.obtener_ubicacion_estimada(paquete)
            }
        return None
    
    def obtener_ubicacion_estimada(self, paquete):
        # Lógica para estimar ubicación basada en ruta asignada
        return {"descripcion": "En ruta hacia destino", "precision": "ciudad"}
    
    def generar_metricas_rendimiento(self):
        total_paquetes = len(self.paquetes)
        entregados = sum(1 for p in self.paquetes.values() if p.estado == "entregado")
        
        tiempo_promedio_entrega = 0  # Calcularía basado en fechas
        
        return {
            'total_paquetes': total_paquetes,
            'paquetes_entregados': entregados,
            'tasa_entrega': entregados / total_paquetes if total_paquetes > 0 else 0,
            'tiempo_promedio_entrega_horas': tiempo_promedio_entrega,
            'rutas_activas': len(self.rutas_activas)
        }