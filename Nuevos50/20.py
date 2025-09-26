class Instrumento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.afinado = True
    
    def tocar(self):
        raise NotImplementedError
    
    def afinar(self):
        self.afinado = True

class Guitarra(Instrumento):
    def __init__(self, nombre="Guitarra", cuerdas=6):
        super().__init__(nombre, "Cuerda")
        self.cuerdas = cuerdas
    
    def tocar(self):
        return "♪ Strumming guitar chords ♪"
    
    def cambiar_cuerda(self, numero_cuerda):
        return f"Cambiando cuerda {numero_cuerda}"

class Piano(Instrumento):
    def __init__(self, nombre="Piano", teclas=88):
        super().__init__(nombre, "Teclado")
        self.teclas = teclas
    
    def tocar(self):
        return "♪ Playing beautiful melodies ♪"
    
    def presionar_pedal(self):
        return "Pedal pressed for sustain"

class Bateria(Instrumento):
    def __init__(self, nombre="Batería"):
        super().__init__(nombre, "Percusión")
        self.tambores = ["kick", "snare", "hi-hat", "tom"]
    
    def tocar(self):
        return "♪ Boom! Crash! ♪"
    
    def golpear_tambor(self, tambor):
        if tambor in self.tambores:
            return f"Golpeando {tambor}"
        return "Tambor no encontrado"