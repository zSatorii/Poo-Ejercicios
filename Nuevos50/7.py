class Contador:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
        self.inicial = valor_inicial
    
    def incrementar(self):
        self.valor += 1
    
    def decrementar(self):
        self.valor -= 1
    
    def reset(self):
        self.valor = self.inicial
    
    def obtener_valor(self):
        return self.valor