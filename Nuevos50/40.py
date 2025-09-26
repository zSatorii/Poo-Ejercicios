class PerfilUsuario:
    def __init__(self, nombre, email, privacidad="publico"):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.privacidad = privacidad
        self.amigos = set()
        self.publicaciones = []
        self.grupos = []
        self.notificaciones = []
    
    def enviar_solicitud_amistad(self, usuario):
        notificacion = Notificacion(
            f"{self.nombre} te envió una solicitud de amistad",
            "solicitud_amistad",
            self
        )
        usuario.notificaciones.append(notificacion)
    
    def aceptar_amistad(self, usuario):
        self.amigos.add(usuario)
        usuario.amigos.add(self)

class PublicacionAvanzada:
    def __init__(self, autor, contenido, tipo="texto"):
        self.id = str(uuid.uuid4())
        self.autor = autor
        self.contenido = contenido
        self.tipo = tipo  # texto, imagen, video
        self.fecha = datetime.now()
        self.likes = set()
        self.comentarios = []
        self.compartido_por = []
        self.privacidad = "publico"
    
    def compartir(self, usuario):
        if usuario not in self.compartido_por:
            self.compartido_por.append(usuario)

class Grupo:
    def __init__(self, nombre, descripcion, admin):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.admin = admin
        self.miembros = [admin]
        self.publicaciones = []
        self.privacidad = "publico"  # publico, privado, secreto
    
    def unirse(self, usuario):
        if self.privacidad == "publico":
            self.miembros.append(usuario)
            usuario.grupos.append(self)
            return True
        return False

class Notificacion:
    def __init__(self, mensaje, tipo, remitente=None):
        self.id = str(uuid.uuid4())
        self.mensaje = mensaje
        self.tipo = tipo
        self.remitente = remitente
        self.fecha = datetime.now()
        self.leida = False
    
    def marcar_leida(self):
        self.leida = True