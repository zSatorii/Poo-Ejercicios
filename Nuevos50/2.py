class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.usuario_actual = None
    
    def prestar(self, usuario):
        if self.disponible:
            self.disponible = False
            self.usuario_actual = usuario
            return f"Libro prestado a {usuario}"
        return "Libro no disponible"
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            usuario = self.usuario_actual
            self.usuario_actual = None
            return f"Libro devuelto por {usuario}"
        return "El libro ya estaba disponible"
