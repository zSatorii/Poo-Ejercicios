class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio
    
    def contar_regresivamente(self):
        actual = self.inicio
        while actual >= 0:
            print(actual)
            actual -= 1

cr = CuentaRegresiva(5)
cr.contar_regresivamente()
