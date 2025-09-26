class Temperatura:
    def __init__(self, valor, escala="C"):
        self.valor = valor
        self.escala = escala.upper()
    
    def a_celsius(self):
        if self.escala == "C":
            return self.valor
        elif self.escala == "F":
            return (self.valor - 32) * 5/9
        else:  # Kelvin
            return self.valor - 273.15
    
    def a_fahrenheit(self):
        celsius = self.a_celsius()
        return celsius * 9/5 + 32
    
    def a_kelvin(self):
        celsius = self.a_celsius()
        return celsius + 273.15