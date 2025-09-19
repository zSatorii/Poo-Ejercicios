class Contador:
    def __init__(self, n):
        self.n = n
    
    def contar(self):
        i = 1
        while i <= self.n:
            print(i)
            i += 1

contador = Contador(5)
contador.contar()
