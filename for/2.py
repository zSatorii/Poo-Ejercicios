class Cuadrados:
    def __init__(self, n):
        self.n = n
    
    def mostrar_cuadrados(self):
        for i in range(1, self.n+1):
            print(i, "al cuadrado es", i*i)

c = Cuadrados(5)
c.mostrar_cuadrados()
