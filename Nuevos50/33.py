# EJERCICIO 33: Sistema de Pedidos
class DetallePedido:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    
    def subtotal(self):
        return self.cantidad * self.precio_unitario

class Pedido:
    def __init__(self, cliente, numero_pedido):
        self.cliente = cliente
        self.numero_pedido = numero_pedido
        self.fecha_pedido = datetime.now()
        self.estado = "pendiente"  # pendiente, procesando, enviado, entregado
        self.detalles = []
        self.direccion_envio = ""
    
    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
    
    def calcular_total(self):
        return sum(detalle.subtotal() for detalle in self.detalles)
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["pendiente", "procesando", "enviado", "entregado", "cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return True
        return False

class Cliente:
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.pedidos = []
    
    def crear_pedido(self, numero_pedido):
        pedido = Pedido(self, numero_pedido)
        self.pedidos.append(pedido)
        return pedido

class SistemaPedidos:
    def __init__(self):
        self.clientes = {}
        self.pedidos = {}
        self.productos = {}
    
    def procesar_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            pedido = self.pedidos[numero_pedido]
            if pedido.estado == "pendiente":
                pedido.cambiar_estado("procesando")
                return f"Pedido {numero_pedido} está siendo procesado"
        return "Pedido no encontrado o ya procesado"
    
    def rastrear_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            pedido = self.pedidos[numero_pedido]
            return {
                'numero': pedido.numero_pedido,
                'estado': pedido.estado,
                'fecha': pedido.fecha_pedido,
                'total': pedido.calcular_total()
            }
        return None