import time

class Cronometro:
    def __init__(self):
        self.tiempo_inicio = 0
        self.tiempo_pausado = 0
        self.corriendo = False
        self.vueltas = []
    
    def iniciar(self):
        self.tiempo_inicio = time.time()
        self.corriendo = True
    
    def pausar(self):
        if self.corriendo:
            self.tiempo_pausado += time.time() - self.tiempo_inicio
            self.corriendo = False
    
    def detener(self):
        self.corriendo = False
        self.tiempo_pausado = 0
        self.vueltas = []
    
    def vuelta(self):
        if self.corriendo:
            tiempo_vuelta = time.time() - self.tiempo_inicio + self.tiempo_pausado
            self.vueltas.append(tiempo_vuelta)
