class ContenidoStreaming:
    def __init__(self, titulo, descripcion, duracion, genero, clasificacion):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descripcion = descripcion
        self.duracion = duracion  # en minutos
        self.genero = genero
        self.clasificacion = clasificacion
        self.calificaciones = []
        self.visualizaciones = 0
    
    def reproducir(self, usuario):
        self.visualizaciones += 1
        visualizacion = {
            'usuario': usuario.id,
            'fecha': datetime.now(),
            'duracion_vista': 0
        }
        return visualizacion

class Playlist:
    def __init__(self, nombre, usuario, publica=False):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.usuario = usuario
        self.contenidos = []
        self.publica = publica
        self.fecha_creacion = datetime.now()
    
    def agregar_contenido(self, contenido):
        if contenido not in self.contenidos:
            self.contenidos.append(contenido)
    
    def duracion_total(self):
        return sum(contenido.duracion for contenido in self.contenidos)

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.playlists = []
        self.historial_visualizacion = []
        self.preferencias = []
    
    def ver_contenido(self, contenido):
        if self.suscripcion.permite_contenido(contenido):
            visualizacion = contenido.reproducir(self)
            self.historial_visualizacion.append(visualizacion)
            return True
        return False

class Suscripcion:
    def __init__(self, tipo, precio_mensual, contenido_premium=False):
        self.tipo = tipo  # basico, premium, familiar
        self.precio_mensual = precio_mensual
        self.contenido_premium = contenido_premium
        self.dispositivos_simultaneos = {"basico": 1, "premium": 2, "familiar": 4}.get(tipo, 1)
    
    def permite_contenido(self, contenido):
        if contenido.clasificacion == "premium":
            return self.contenido_premium
        return True

class AlgoritmoRecomendacion:
    @staticmethod
    def recomendar_contenido(usuario, catalogo):
        # Algoritmo simple basado en géneros vistos
        generos_favoritos = {}
        for vis in usuario.historial_visualizacion[-10:]:  # Últimas 10 visualizaciones
            # Simplificado: asumir que tenemos acceso al contenido
            pass
        
        recomendaciones = [c for c in catalogo if c.genero in generos_favoritos][:10]
        return recomendaciones