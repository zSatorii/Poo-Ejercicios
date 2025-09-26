class ConversorMonedas:
    def __init__(self):
        self.tasas = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 110.0,
            'COP': 4000.0
        }
        self.historial = []
    
    def convertir(self, cantidad, de_moneda, a_moneda):
        if de_moneda in self.tasas and a_moneda in self.tasas:
            # Convertir a USD primero, luego a la moneda destino
            cantidad_usd = cantidad / self.tasas[de_moneda]
            resultado = cantidad_usd * self.tasas[a_moneda]
            
            self.historial.append(f"{cantidad} {de_moneda} = {resultado:.2f} {a_moneda}")
            return resultado
        return "Moneda no soportada"
    
    def actualizar_tasa(self, moneda, nueva_tasa):
        self.tasas[moneda] = nueva_tasa