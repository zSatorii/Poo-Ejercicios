class Termostato:
    def __init__(self):
        self.temperatura_objetivo = 20
        self.temperatura_actual = 18
        self.encendido = True
    
    def establecer_temperatura(self, temp):
        self.temperatura_objetivo = temp
    
    def obtener_temperatura(self):
        return self.temperatura_actual
    
    def actualizar(self):
        if self.encendido:
            if self.temperatura_actual < self.temperatura_objetivo:
                self.temperatura_actual += 0.5  # Calentar
            elif self.temperatura_actual > self.temperatura_objetivo:
                self.temperatura_actual -= 0.5  # Enfriar
    
    def encender(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False
