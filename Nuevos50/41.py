class CuentaBancariaCompleta:
    def __init__(self, numero_cuenta, titular, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0
        self.estado = "activa"
        self.transacciones = []
        self.fecha_apertura = datetime.now()
    
    def realizar_transaccion(self, tipo, monto, descripcion=""):
        if self.estado != "activa":
            return False
        
        transaccion = Transaccion(tipo, monto, self, descripcion)
        
        if tipo == "deposito":
            self.saldo += monto
        elif tipo == "retiro" and self.saldo >= monto:
            self.saldo -= monto
        else:
            return False
        
        self.transacciones.append(transaccion)
        return True

class Transaccion:
    def __init__(self, tipo, monto, cuenta, descripcion=""):
        self.id = str(uuid.uuid4())
        self.tipo = tipo
        self.monto = monto
        self.cuenta = cuenta
        self.descripcion = descripcion
        self.fecha = datetime.now()
        self.procesada = True

class TarjetaBancaria:
    def __init__(self, numero, tipo, cuenta, limite=None):
        self.numero = numero
        self.tipo = tipo  # debito, credito
        self.cuenta = cuenta
        self.limite = limite
        self.activa = True
        self.cvv = "123"  # Simplificado
    
    def procesar_compra(self, monto):
        if not self.activa:
            return False
        
        if self.tipo == "debito":
            return self.cuenta.realizar_transaccion("retiro", monto, "Compra con tarjeta")
        elif self.tipo == "credito" and monto <= self.limite:
            return True
        return False

class Prestamo:
    def __init__(self, monto, tasa_interes, plazo_meses, cuenta):
        self.id = str(uuid.uuid4())
        self.monto_original = monto
        self.monto_pendiente = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo_meses
        self.cuenta = cuenta
        self.cuota_mensual = self.calcular_cuota()
        self.pagos_realizados = []
    
    def calcular_cuota(self):
        # Fórmula de cuota fija
        r = self.tasa_interes / 12  # Tasa mensual
        if r == 0:
            return self.monto_original / self.plazo_meses
        return self.monto_original * r * (1 + r) ** self.plazo_meses / ((1 + r) ** self.plazo_meses - 1)
    
    def realizar_pago(self, monto):
        if monto >= self.cuota_mensual:
            interes = self.monto_pendiente * (self.tasa_interes / 12)
            capital = monto - interes
            self.monto_pendiente -= capital
            
            pago = {
                'fecha': datetime.now(),
                'monto': monto,
                'capital': capital,
                'interes': interes,
                'saldo_pendiente': self.monto_pendiente
            }
            self.pagos_realizados.append(pago)
            return pago
        return None
