class ContadorVocales:
    def __init__(self, palabra):
        self.palabra = palabra
    
    def contar(self):
        contador = 0
        for letra in self.palabra:
            if letra.lower() in "aeiou":
                contador += 1
        return contador

cv = ContadorVocales("python")
print(cv.contar())
