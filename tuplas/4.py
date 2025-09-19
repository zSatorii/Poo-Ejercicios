class TuplaALista:
    def __init__(self, tupla):
        self.tupla = tupla

    def a_lista(self):
        return list(self.tupla)

tl = TuplaALista((5, 2, 9))
print(tl.a_lista())
