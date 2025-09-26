class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.activo = True
    
    def puede_hacer(self, accion):
        return False  # Por defecto sin permisos

class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.permisos = ["crear", "leer", "actualizar", "eliminar", "administrar"]
    
    def puede_hacer(self, accion):
        return accion in self.permisos

class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.permisos = ["leer", "comprar"]
    
    def puede_hacer(self, accion):
        return accion in self.permisos

class Moderador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.permisos = ["leer", "actualizar", "moderar"]
    
    def puede_hacer(self, accion):
        return accion in self.permisos