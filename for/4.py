class MultiplosTres:
    def __init__(self, n):
        self.n = n
    
    def obtener_multiplos(self):
        multiplos = []
        for i in range(1, self.n+1):
            if i % 3 == 0:
                multiplos.append(i)
        return multiplos

mt = MultiplosTres(20)
print(mt.obtener_multiplos())
