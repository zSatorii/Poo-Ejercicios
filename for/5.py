class Promedios:
    def __init__(self, listas):
        self.listas = listas

    def promediar(self):
        for lista in self.listas:
            suma = 0
            for n in lista:
                suma += n
            promedio = suma / len(lista)
            print(f"Promedio: {promedio}")

prom = Promedios([[1,2,3],[4,5,6,7],[10,15]])
prom.promediar()
