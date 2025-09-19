class ContadorPares:
    def __init__(self, lista):
        self.lista = lista
    
    def contar_pares(self):
        i = 0
        contador = 0
        while i < len(self.lista):
            if self.lista[i] % 2 == 0:
                contador += 1
            i += 1
        return contador

cp = ContadorPares([1,2,3,4,5,6])
print(cp.contar_pares())
