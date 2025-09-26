class Reloj:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._validar()
    
    def _validar(self):
        if self.segundos >= 60:
            self.minutos += self.segundos // 60
            self.segundos %= 60
        if self.minutos >= 60:
            self.horas += self.minutos // 60
            self.minutos %= 60
        if self.horas >= 24:
            self.horas %= 24
    
    def avanzar_segundo(self):
        self.segundos += 1
        self._validar()
    
    def mostrar_tiempo(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
