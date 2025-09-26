class ReproductorMusica:
    def __init__(self):
        self.canciones = []
        self.cancion_actual = 0
        self.reproduciendo = False
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    def reproducir(self):
        if self.canciones:
            self.reproduciendo = True
            return f"Reproduciendo: {self.canciones[self.cancion_actual]}"
        return "No hay canciones"
    
    def pausar(self):
        self.reproduciendo = False
    
    def siguiente(self):
        if self.canciones:
            self.cancion_actual = (self.cancion_actual + 1) % len(self.canciones)
    
    def anterior(self):
        if self.canciones:
            self.cancion_actual = (self.cancion_actual - 1) % len(self.canciones)