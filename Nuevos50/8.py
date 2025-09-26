class Lampara:
    def __init__(self):
        self.encendida = False
        self.intensidad = 100
        self.color = "blanco"
    
    def encender(self):
        self.encendida = True
    
    def apagar(self):
        self.encendida = False
    
    def cambiar_intensidad(self, intensidad):
        if 0 <= intensidad <= 100:
            self.intensidad = intensidad
    
    def cambiar_color(self, color):
        self.color = color
    
    def estado(self):
        return f"Encendida: {self.encendida}, Intensidad: {self.intensidad}%, Color: {self.color}"
