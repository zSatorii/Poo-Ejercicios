from datetime import datetime, timedelta

class LibroDigital:
    def __init__(self, titulo, autor, isbn, tipo="libro"):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.tipo = tipo  # libro, revista, DVD
        self.disponible = True
    
    def dias_prestamo(self):
        dias = {"libro": 14, "revista": 7, "DVD": 3}
        return dias.get(self.tipo, 14)

class UsuarioBiblioteca:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos_activos = []
        self.multas = 0
    
    def puede_prestar(self):
        return len(self.prestamos_activos) < 5 and self.multas == 0

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=libro.dias_prestamo())
        self.fecha_devolucion = None
    
    def esta_vencido(self):
        return datetime.now() > self.fecha_vencimiento and not self.fecha_devolucion
    
    def calcular_multa(self):
        if self.esta_vencido():
            dias_retraso = (datetime.now() - self.fecha_vencimiento).days
            return dias_retraso * 1000  # $1000 por día
        return 0

class BibliotecaDigital:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []
    
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            
            if libro.disponible and usuario.puede_prestar():
                prestamo = Prestamo(libro, usuario)
                libro.disponible = False
                usuario.prestamos_activos.append(prestamo)
                self.prestamos.append(prestamo)
                return prestamo
        return None
    
    def devolver_libro(self, prestamo):
        prestamo.fecha_devolucion = datetime.now()
        prestamo.libro.disponible = True
        prestamo.usuario.prestamos_activos.remove(prestamo)
        
        # Aplicar multa si es necesario
        multa = prestamo.calcular_multa()
        if multa > 0:
            prestamo.usuario.multas += multa
        
        return multa
