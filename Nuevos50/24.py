class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historial = []
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        self.historial.append(f"Depósito: +${cantidad}")
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            self.historial.append(f"Retiro: -${cantidad}")
            return True
        return False

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.02):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes
    
    def calcular_interes(self):
        interes = self.saldo * self.tasa_interes
        self.depositar(interes)
        return interes

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, limite_sobregiro=500):
        super().__init__(titular, saldo_inicial)
        self.limite_sobregiro = limite_sobregiro
    
    def retirar(self, cantidad):
        if self.saldo + self.limite_sobregiro >= cantidad:
            self.saldo -= cantidad
            self.historial.append(f"Retiro: -${cantidad}")
            if self.saldo < 0:
                self.historial.append("Cuenta en sobregiro")
            return True
        return False
