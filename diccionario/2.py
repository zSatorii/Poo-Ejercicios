class Agenda:
    def __init__(self, propietario):
        self.propietario = propietario
        self.contactos = {} 
    
    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado")
    
    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"{nombre}: {self.contactos[nombre]}")
        else:
            print("Contacto no encontrado")
    
    def mostrar_todos(self):
        print(f"Agenda de {self.propietario}:")
        for nombre, telefono in self.contactos.items():
            print(f"{nombre}: {telefono}")

agenda1 = Agenda("María")
agenda1.agregar_contacto("Juan", "3001234567")
agenda1.agregar_contacto("Ana", "3109876543")
agenda1.buscar_contacto("Juan")
agenda1.mostrar_todos()
