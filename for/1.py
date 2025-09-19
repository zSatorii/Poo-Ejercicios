class SumaLista:
    def __init__(self, lista):
        self.lista = lista
    
    def suma(self):
        total = 0
        for n in self.lista:
            total += n
        return total

sl = SumaLista([1,2,3,4,5])
print(sl.suma())
