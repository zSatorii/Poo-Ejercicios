import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefonos = [telefono] if isinstance(telefono, str) else telefono
        self.email = email
        self.valido = self.validar()
    
    def validar(self):
        # Validar email
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email_valido = re.match(patron_email, self.email) is not None
        
        # Validar teléfonos
        patron_telefono = r'^\+?[\d\s\-\(\)]{7,15}$'
        telefonos_validos = all(re.match(patron_telefono, tel) for tel in self.telefonos)
        
        return email_valido and telefonos_validos
    
    def agregar_telefono(self, telefono):
        if telefono not in self.telefonos:
            self.telefonos.append(telefono)
    
    def __str__(self):
        return f"{self.nombre}: {', '.join(self.telefonos)} - {self.email}"

class AgendaTelefonica:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
    
    def buscar_por_nombre(self, nombre):
        return [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
    
    def buscar_por_telefono(self, telefono):
        return [c for c in self.contactos if telefono in c.telefonos]