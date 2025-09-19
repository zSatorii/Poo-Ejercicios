class ContadorCaracteres:
    def __init__(self, texto):
        self.texto = texto
    
    def contar(self):
        contador = 0
        i = 0
        while i < len(self.texto):
            contador += 1
            i += 1
        return contador

contador = ContadorCaracteres("hola mundo")
print(contador.contar())
