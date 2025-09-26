class ElementoSistema:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fecha_creacion = datetime.now()
    
    def obtener_tamaño(self):
        raise NotImplementedError

class Archivo(ElementoSistema):
    def __init__(self, nombre, contenido=""):
        super().__init__(nombre)
        self.contenido = contenido
    
    def obtener_tamaño(self):
        return len(self.contenido)
    
    def escribir(self, texto):
        self.contenido = texto
    
    def leer(self):
        return self.contenido

class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []
    
    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)
    
    def eliminar_elemento(self, nombre):
        self.elementos = [e for e in self.elementos if e.nombre != nombre]
    
    def obtener_tamaño(self):
        return sum(elemento.obtener_tamaño() for elemento in self.elementos)
    
    def buscar(self, nombre):
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                return elemento
            if isinstance(elemento, Carpeta):
                resultado = elemento.buscar(nombre)
                if resultado:
                    return resultado
        return None