class Buscador:
    def __init__(self, lista, valor):
        self.lista = lista
        self.valor = valor
    
    def buscar(self):
        i = 0
        encontrado = False
        while i < len(self.lista):
            if self.lista[i] == self.valor:
                encontrado = True
                break
            i += 1
        return encontrado

buscador = Buscador([3,5,7,9], 7)
print(buscador.buscar())  # True
