class DiccionarioPersonal:
    def __init__(self, idioma):
        self.idioma = idioma
        self.palabras = {}
    
    def agregar_palabra(self, palabra, definicion):
        self.palabras[palabra] = definicion
        print(f"Palabra '{palabra}' agregada")
    
    def buscar_palabra(self, palabra):
        if palabra in self.palabras:
            print(f"{palabra}: {self.palabras[palabra]}")
        else:
            print("Palabra no encontrada")
    
    def contar_palabras(self):
        total = len(self.palabras)
        print(f"Total de palabras en {self.idioma}: {total}")
    
    def mostrar_todas(self):
        print(f"Diccionario de {self.idioma}:")
        for palabra, definicion in self.palabras.items():
            print(f"{palabra}: {definicion}")

diccionario1 = DiccionarioPersonal("Inglés")
diccionario1.agregar_palabra("hello", "hola")
diccionario1.agregar_palabra("book", "libro")
diccionario1.buscar_palabra("hello")
diccionario1.contar_palabras()
diccionario1.mostrar_todas()
