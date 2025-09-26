class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.seguidos = set()
        self.seguidores = set()
        self.publicaciones = []
    
    def seguir(self, usuario):
        self.seguidos.add(usuario)
        usuario.seguidores.add(self)
    
    def dejar_seguir(self, usuario):
        self.seguidos.discard(usuario)
        usuario.seguidores.discard(self)
    
    def publicar(self, contenido):
        publicacion = Publicacion(contenido, self)
        self.publicaciones.append(publicacion)
        return publicacion

class Publicacion:
    def __init__(self, contenido, autor):
        self.contenido = contenido
        self.autor = autor
        self.fecha = datetime.now()
        self.likes = set()
        self.comentarios = []
    
    def dar_like(self, usuario):
        self.likes.add(usuario)
    
    def quitar_like(self, usuario):
        self.likes.discard(usuario)
    
    def comentar(self, usuario, texto):
        comentario = Comentario(texto, usuario)
        self.comentarios.append(comentario)
        return comentario

class Comentario:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor
        self.fecha = datetime.now()
