import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras
        self.lanzamientos = []
    
    def lanzar(self):
        resultado = random.randint(1, self.caras)
        self.lanzamientos.append(resultado)
        return resultado
    
    def obtener_estadisticas(self):
        if not self.lanzamientos:
            return "Sin lanzamientos"
        return {
            'total': len(self.lanzamientos),
            'promedio': sum(self.lanzamientos) / len(self.lanzamientos)
        }