class Freelancer:
    def __init__(self, nombre, email, habilidades, tarifa_hora):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.habilidades = habilidades
        self.tarifa_hora = tarifa_hora
        self.calificacion_promedio = 0
        self.proyectos_completados = 0
        self.portafolio = []
        self.disponible = True
        self.ubicacion = ""
    
    def agregar_portafolio(self, proyecto_muestra):
        self.portafolio.append(proyecto_muestra)
    
    def actualizar_calificacion(self, nueva_calificacion):
        total_puntos = self.calificacion_promedio * self.proyectos_completados
        self.proyectos_completados += 1
        self.calificacion_promedio = (total_puntos + nueva_calificacion) / self.proyectos_completados

class ClienteFreelance:
    def __init__(self, nombre, email, empresa=None):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.empresa = empresa
        self.proyectos_publicados = []
        self.calificacion_como_cliente = 0
        self.verificado = False

class ProyectoFreelance:
    def __init__(self, cliente, titulo, descripcion, presupuesto, fecha_limite, habilidades_requeridas):
        self.id = str(uuid.uuid4())
        self.cliente = cliente
        self.titulo = titulo
        self.descripcion = descripcion
        self.presupuesto = presupuesto
        self.fecha_limite = fecha_limite
        self.habilidades_requeridas = habilidades_requeridas
        self.estado = "abierto"
        self.propuestas = []
        self.freelancer_seleccionado = None
        self.fecha_publicacion = datetime.now()
    
    def recibir_propuesta(self, propuesta):
        if self.estado == "abierto":
            self.propuestas.append(propuesta)
    
    def seleccionar_freelancer(self, freelancer):
        self.freelancer_seleccionado = freelancer
        self.estado = "en_progreso"
        freelancer.disponible = False

class Propuesta:
    def __init__(self, freelancer, proyecto, precio_propuesto, tiempo_entrega, mensaje):
        self.id = str(uuid.uuid4())
        self.freelancer = freelancer
        self.proyecto = proyecto
        self.precio_propuesto = precio_propuesto
        self.tiempo_entrega = tiempo_entrega  # en días
        self.mensaje = mensaje
        self.fecha_propuesta = datetime.now()
        self.estado = "enviada"

class SistemaMatching:
    @staticmethod
    def buscar_freelancers_compatibles(proyecto):
        # Algoritmo simple de matching basado en habilidades
        freelancers_compatibles = []
        
        # Simular base de datos de freelancers
        freelancers_disponibles = []  # Se llenaría desde la base de datos
        
        for freelancer in freelancers_disponibles:
            if freelancer.disponible:
                habilidades_coincidentes = set(freelancer.habilidades) & set(proyecto.habilidades_requeridas)
                porcentaje_coincidencia = len(habilidades_coincidentes) / len(proyecto.habilidades_requeridas)
                
                if porcentaje_coincidencia >= 0.5:  # Al menos 50% de coincidencia
                    freelancers_compatibles.append({
                        'freelancer': freelancer,
                        'coincidencia': porcentaje_coincidencia,
                        'tarifa_compatible': freelancer.tarifa_hora <= proyecto.presupuesto / 40  # Estimando 40 horas
                    })
        
        return sorted(freelancers_compatibles, key=lambda x: x['coincidencia'], reverse=True)

class PlataformaFreelancing:
    def __init__(self):
        self.freelancers = {}
        self.clientes = {}
        self.proyectos = {}
        self.transacciones = []
        self.disputas = []
    
    def procesar_pago(self, proyecto, cantidad):
        # Sistema de escrow simplificado
        transaccion = {
            'id': str(uuid.uuid4()),
            'proyecto': proyecto.id,
            'cliente': proyecto.cliente.id,
            'freelancer': proyecto.freelancer_seleccionado.id,
            'cantidad': cantidad,
            'fecha': datetime.now(),
            'estado': 'en_escrow'
        }
        
        self.transacciones.append(transaccion)
        return transaccion
    
    def liberar_pago(self, transaccion_id):
        for transaccion in self.transacciones:
            if transaccion['id'] == transaccion_id:
                transaccion['estado'] = 'completada'
                return True
        return False