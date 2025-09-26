import random

class Accion:
    def __init__(self, simbolo, nombre_empresa, precio_inicial, volatilidad=0.02):
        self.simbolo = simbolo
        self.nombre_empresa = nombre_empresa
        self.precio_actual = precio_inicial
        self.volatilidad = volatilidad
        self.historial_precios = [precio_inicial]
        self.volumen_diario = 0
    
    def actualizar_precio(self):
        # Simulación de movimiento de precio (Random Walk)
        cambio_porcentual = random.gauss(0, self.volatilidad)
        nuevo_precio = self.precio_actual * (1 + cambio_porcentual)
        self.precio_actual = max(0.01, nuevo_precio)  # Precio mínimo
        self.historial_precios.append(self.precio_actual)
    
    def obtener_rendimiento(self, dias):
        if len(self.historial_precios) > dias:
            precio_inicial = self.historial_precios[-dias]
            return (self.precio_actual - precio_inicial) / precio_inicial
        return 0

class Portafolio:
    def __init__(self, usuario, saldo_inicial):
        self.usuario = usuario
        self.saldo_efectivo = saldo_inicial
        self.posiciones = {}  # simbolo: cantidad
        self.historial_transacciones = []
        self.valor_inicial = saldo_inicial
    
    def comprar_accion(self, accion, cantidad):
        costo_total = accion.precio_actual * cantidad
        if self.saldo_efectivo >= costo_total:
            self.saldo_efectivo -= costo_total
            
            if accion.simbolo in self.posiciones:
                self.posiciones[accion.simbolo] += cantidad
            else:
                self.posiciones[accion.simbolo] = cantidad
            
            transaccion = {
                'tipo': 'compra',
                'simbolo': accion.simbolo,
                'cantidad': cantidad,
                'precio': accion.precio_actual,
                'fecha': datetime.now()
            }
            self.historial_transacciones.append(transaccion)
            return True
        return False
    
    def vender_accion(self, accion, cantidad):
        if accion.simbolo in self.posiciones and self.posiciones[accion.simbolo] >= cantidad:
            ingresos = accion.precio_actual * cantidad
            self.saldo_efectivo += ingresos
            self.posiciones[accion.simbolo] -= cantidad
            
            if self.posiciones[accion.simbolo] == 0:
                del self.posiciones[accion.simbolo]
            
            transaccion = {
                'tipo': 'venta',
                'simbolo': accion.simbolo,
                'cantidad': cantidad,
                'precio': accion.precio_actual,
                'fecha': datetime.now()
            }
            self.historial_transacciones.append(transaccion)
            return True
        return False
    
    def calcular_valor_total(self, mercado):
        valor_acciones = sum(
            mercado.obtener_accion(simbolo).precio_actual * cantidad
            for simbolo, cantidad in self.posiciones.items()
        )
        return self.saldo_efectivo + valor_acciones
    
    def calcular_pnl(self, mercado):
        valor_actual = self.calcular_valor_total(mercado)
        return valor_actual - self.valor_inicial

class Mercado:
    def __init__(self):
        self.acciones = {}
        self.indice_mercado = 1000
        self.abierto = False
    
    def agregar_accion(self, accion):
        self.acciones[accion.simbolo] = accion
    
    def obtener_accion(self, simbolo):
        return self.acciones.get(simbolo)
    
    def actualizar_mercado(self):
        for accion in self.acciones.values():
            accion.actualizar_precio()
        
        # Actualizar índice del mercado
        cambio_promedio = sum(
            (accion.historial_precios[-1] - accion.historial_precios[-2]) / accion.historial_precios[-2]
            for accion in self.acciones.values()
            if len(accion.historial_precios) > 1
        ) / len(self.acciones) if self.acciones else 0
        
        self.indice_mercado *= (1 + cambio_promedio)

class EstrategiaTrading:
    @staticmethod
    def media_movil_simple(accion, periodo):
        if len(accion.historial_precios) >= periodo:
            precios_recientes = accion.historial_precios[-periodo:]
            return sum(precios_recientes) / periodo
        return accion.precio_actual
    
    @staticmethod
    def señal_compra_venta(accion, periodo_corto=5, periodo_largo=20):
        if len(accion.historial_precios) >= periodo_largo:
            media_corta = EstrategiaTrading.media_movil_simple(accion, periodo_corto)
            media_larga = EstrategiaTrading.media_movil_simple(accion, periodo_largo)
            
            if media_corta > media_larga:
                return "COMPRA"
            elif media_corta < media_larga:
                return "VENTA"
        return "MANTENER"