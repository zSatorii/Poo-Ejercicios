class Avatar:
    def __init__(self, nombre, usuario_id):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.posicion = {"x": 0, "y": 0, "z": 0}
        self.orientacion = {"pitch": 0, "yaw": 0, "roll": 0}
        self.apariencia = {
            "modelo_3d": "avatar_basico",
            "textura": "piel_1",
            "ropa": ["camisa_azul", "pantalon_negro"],
            "accesorios": []
        }
        self.inventario = []
        self.nivel_energia = 100
        self.habilidades = {}
        self.amigos = set()
        self.estado = "activo"
    
    def mover_a(self, nueva_posicion):
        distancia = self.calcular_distancia(self.posicion, nueva_posicion)
        energia_necesaria = distancia * 0.1
        
        if self.nivel_energia >= energia_necesaria:
            self.posicion = nueva_posicion
            self.nivel_energia -= energia_necesaria
            return True
        return False
    
    def calcular_distancia(self, pos1, pos2):
        return math.sqrt((pos1["x"] - pos2["x"])**2 + 
                        (pos1["y"] - pos2["y"])**2 + 
                        (pos1["z"] - pos2["z"])**2)
    
    def cambiar_apariencia(self, aspecto, nuevo_valor):
        if aspecto in self.apariencia:
            self.apariencia[aspecto] = nuevo_valor
    
    def usar_objeto(self, objeto):
        if objeto in self.inventario:
            resultado = objeto.usar(self)
            return resultado
        return False

class Objeto3D:
    def __init__(self, nombre, tipo, posicion, propiedades):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.tipo = tipo
        self.posicion = posicion
        self.propiedades = propiedades
        self.propietario = None
        self.precio_nft = 0
        self.rareza = "común"
        self.metadata_blockchain = {}
    
    def interactuar(self, avatar):
        """Define cómo el avatar puede interactuar con el objeto"""
        if self.tipo == "funcional":
            return self.ejecutar_funcion(avatar)
        elif self.tipo == "coleccionable":
            return avatar.inventario.append(self)
        return False
    
    def ejecutar_funcion(self, avatar):
        """Funciones específicas según el tipo de objeto"""
        if "teleporter" in self.nombre.lower():
            destino = self.propiedades.get("destino", {"x": 0, "y": 0, "z": 0})
            return avatar.mover_a(destino)
        elif "regenerador" in self.nombre.lower():
            avatar.nivel_energia = 100
            return True
        return False
    
    def convertir_a_nft(self, precio):
        """Convierte el objeto en NFT para comercio"""
        self.precio_nft = precio
        self.metadata_blockchain = {
            "nombre": self.nombre,
            "descripcion": f"{self.tipo} de rareza {self.rareza}",
            "imagen": f"imagen_{self.id}.png",
            "atributos": self.propiedades,
            "creador": self.propietario,
            "fecha_creacion": datetime.now().isoformat()
        }

class MundoVirtual:
    def __init__(self, nombre, dimensiones):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.dimensiones = dimensiones
        self.avatares_presentes = {}
        self.objetos = {}
        self.zonas = {}
        self.fisica = FisicaVirtual()
        self.economia = EconomiaVirtual()
        self.eventos_activos = []
        self.tiempo_virtual = datetime.now()
        self.clima = {"temperatura": 22, "humedad": 50, "viento": 0}
    
    def teletransportar_avatar(self, avatar, posicion):
        if self.posicion_valida(posicion):
            avatar.posicion = posicion
            self.avatares_presentes[avatar.id] = avatar
            return True
        return False
    
    def posicion_valida(self, posicion):
        return (0 <= posicion["x"] <= self.dimensiones["x"] and
                0 <= posicion["y"] <= self.dimensiones["y"] and
                0 <= posicion["z"] <= self.dimensiones["z"])
    
    def crear_objeto(self, nombre, tipo, posicion, creador):
        if self.posicion_valida(posicion):
            objeto = Objeto3D(nombre, tipo, posicion, {})
            objeto.propietario = creador
            self.objetos[objeto.id] = objeto
            return objeto
        return None
    
    def obtener_avatares_cercanos(self, avatar, radio=10):
        avatares_cercanos = []
        for otro_avatar in self.avatares_presentes.values():
            if otro_avatar != avatar:
                distancia = avatar.calcular_distancia(avatar.posicion, otro_avatar.posicion)
                if distancia <= radio:
                    avatares_cercanos.append(otro_avatar)
        return avatares_cercanos
    
    def crear_evento(self, nombre, descripcion, duracion, organizador):
        evento = EventoVirtual(nombre, descripcion, duracion, organizador)
        self.eventos_activos.append(evento)
        return evento

class FisicaVirtual:
    def __init__(self):
        self.gravedad = -9.8
        self.friccion = 0.1
        self.colisiones_activas = True
    
    def aplicar_gravedad(self, objeto):
        if objeto.posicion["z"] > 0 and "volar" not in objeto.propiedades:
            objeto.posicion["z"] += self.gravedad * 0.1
            objeto.posicion["z"] = max(0, objeto.posicion["z"])
    
    def detectar_colision(self, objeto1, objeto2):
        distancia_minima = 1.0
        distancia_actual = math.sqrt(
            (objeto1.posicion["x"] - objeto2.posicion["x"])**2 +
            (objeto1.posicion["y"] - objeto2.posicion["y"])**2 +
            (objeto1.posicion["z"] - objeto2.posicion["z"])**2
        )
        return distancia_actual < distancia_minima

class EconomiaVirtual:
    def __init__(self):
        self.moneda_virtual = "MetaCoin"
        self.tasa_cambio_real = 0.001 
        self.mercado_nft = {}
        self.transacciones = []
        self.impuestos = 0.05
    
    def crear_billetera(self, usuario_id):
        return {
            "usuario_id": usuario_id,
            "saldo": 1000,
            "nfts_poseidos": [],
            "historial_transacciones": []
        }
    
    def comprar_nft(self, comprador, vendedor, nft_id, precio):
        if comprador["saldo"] >= precio:
            impuesto = precio * self.impuestos
            precio_neto = precio - impuesto
            
            comprador["saldo"] -= precio
            vendedor["saldo"] += precio_neto
    
            nft = self.mercado_nft.get(nft_id)
            if nft:
                vendedor["nfts_poseidos"].remove(nft_id)
                comprador["nfts_poseidos"].append(nft_id)
                nft.propietario = comprador["usuario_id"]
                
                transaccion = {
                    "id": str(uuid.uuid4()),
                    "tipo": "compra_nft",
                    "comprador": comprador["usuario_id"],
                    "vendedor": vendedor["usuario_id"],
                    "nft_id": nft_id,
                    "precio": precio,
                    "impuesto": impuesto,
                    "fecha": datetime.now()
                }
                self.transacciones.append(transaccion)
                return transaccion
        return None

class EventoVirtual:
    def __init__(self, nombre, descripcion, duracion, organizador):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.organizador = organizador
        self.participantes = set()
        self.fecha_inicio = datetime.now()
        self.fecha_fin = self.fecha_inicio + timedelta(minutes=duracion)
        self.premios = []
        self.activo = True
    
    def unirse_evento(self, avatar):
        if self.activo and datetime.now() < self.fecha_fin:
            self.participantes.add(avatar.id)
            return True
        return False
    
    def finalizar_evento(self):
        self.activo = False
        return len(self.participantes)

class Metaverso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mundos = {}
        self.usuarios_conectados = {}
        self.servidores = []
        self.estadisticas = {
            "usuarios_totales": 0,
            "mundos_creados": 0,
            "transacciones_nft": 0,
            "tiempo_uso_promedio": 0
        }
    
    def crear_mundo(self, nombre, dimensiones, creador):
        mundo = MundoVirtual(nombre, dimensiones)
        self.mundos[mundo.id] = mundo
        self.estadisticas["mundos_creados"] += 1
        return mundo
    
    def conectar_usuario(self, usuario_id, avatar):
        self.usuarios_conectados[usuario_id] = {
            "avatar": avatar,
            "tiempo_conexion": datetime.now(),
            "mundo_actual": None
        }
        self.estadisticas["usuarios_totales"] += 1
    
    def cambiar_mundo(self, usuario_id, mundo_id):
        if usuario_id in self.usuarios_conectados and mundo_id in self.mundos:
            usuario = self.usuarios_conectados[usuario_id]
            mundo_anterior = usuario["mundo_actual"]
            
            if mundo_anterior:
                avatar = usuario["avatar"]
                if avatar.id in self.mundos[mundo_anterior].avatares_presentes:
                    del self.mundos[mundo_anterior].avatares_presentes[avatar.id]
            

            usuario["mundo_actual"] = mundo_id
            mundo_nuevo = self.mundos[mundo_id]
            mundo_nuevo.avatares_presentes[usuario["avatar"].id] = usuario["avatar"]
            
            return True
        return False
    
    def obtener_estadisticas_globales(self):
        usuarios_activos = len(self.usuarios_conectados)
        mundos_con_actividad = sum(1 for m in self.mundos.values() if len(m.avatares_presentes) > 0)
        
        return {
            "usuarios_activos": usuarios_activos,
            "mundos_con_actividad": mundos_con_actividad,
            "total_mundos": len(self.mundos),
            "eventos_activos": sum(len(m.eventos_activos) for m in self.mundos.values()),
            "objetos_creados": sum(len(m.objetos) for m in self.mundos.values())
        }