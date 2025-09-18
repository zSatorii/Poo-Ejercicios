class ControlLuces:
    def __init__(self, habitacion, estado):
        self.habitacion = habitacion
        self.estado = estado
        self.intensidad = 0
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def ajustar_intensidad(self, nivel):
        self.intensidad = nivel
    
    def verificar_luz(self):
        if self.estado == "encendida":
            print(f"Luz de {self.habitacion}: ENCENDIDA")
            if self.intensidad < 30:
                print("Intensidad: BAJA")
            if self.intensidad >= 30 and self.intensidad < 70:
                print("Intensidad: MEDIA")
            if self.intensidad >= 70:
                print("Intensidad: ALTA")
        if self.estado == "apagada":
            print(f"Luz de {self.habitacion}: APAGADA")
    
    def consumo_energia(self):
        if self.estado == "encendida":
            if self.intensidad < 30:
                print("Consumo: BAJO (5W)")
            if self.intensidad >= 30 and self.intensidad < 70:
                print("Consumo: MEDIO (15W)")
            if self.intensidad >= 70:
                print("Consumo: ALTO (25W)")
        if self.estado == "apagada":
            print("Consumo: 0W")

luz1 = ControlLuces("Sala", "encendida")
luz1.ajustar_intensidad(80)
luz1.verificar_luz()
luz1.consumo_energia()
