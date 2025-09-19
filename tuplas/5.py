class ContarElementos:
    def __init__(self, tupla):
        self.tupla = tupla

    def contar(self):
        return len(self.tupla)

ce = ContarElementos((1, 2, 3, 4))
print(ce.contar())
