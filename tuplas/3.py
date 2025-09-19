class BuscarEnTupla:
    def __init__(self, tupla):
        self.tupla = tupla

    def existe(self, valor):
        return valor in self.tupla

bt = BuscarEnTupla(("rojo", "azul", "verde"))
print(bt.existe("azul"))
print(bt.existe("amarillo"))
