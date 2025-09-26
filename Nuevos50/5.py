class Semaforo:
    def __init__(self):
        self.estados = ["rojo", "amarillo", "verde"]
        self.estado_actual = 0
    
    def cambiar_estado(self):
        self.estado_actual = (self.estado_actual + 1) % len(self.estados)
        return self.estados[self.estado_actual]
    
    def obtener_estado(self):
        return self.estados[self.estado_actual]