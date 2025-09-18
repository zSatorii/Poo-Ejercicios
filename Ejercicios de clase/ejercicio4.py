class vehiculo:
    def __init__(self, motor, llantas, capacidad):
        self.motor = motor
        self.llantas = llantas
        self.capacidad = capacidad
carro1 = vehiculo("1300cc", "rin14", "5 personas")
print(carro1.motor, carro1.llantas, carro1.capacidad)

        