from datetime import datetime
import uuid

class Usuario:
    def __init__(self, nombre, email, password):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.password = password
        self.direcciones = []
        self.metodos_pago = []
        self.historial_compras = []

class Producto:
    def __init__(self, nombre, descripcion, precio, stock, categoria):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.calificaciones = []
        self.activo = True
    
    def agregar_calificacion(self, usuario, puntuacion, comentario):
        self.calificaciones.append({
            'usuario': usuario.nombre,
            'puntuacion': puntuacion,
            'comentario': comentario,
            'fecha': datetime.now()
        })
    
    def promedio_calificaciones(self):
        if self.calificaciones:
            return sum(c['puntuacion'] for c in self.calificaciones) / len(self.calificaciones)
        return 0

class Carrito:
    def __init__(self, usuario):
        self.usuario = usuario
        self.items = {}
        self.descuentos = []
    
    def agregar_item(self, producto, cantidad):
        if producto.id in self.items:
            self.items[producto.id]['cantidad'] += cantidad
        else:
            self.items[producto.id] = {
                'producto': producto,
                'cantidad': cantidad,
                'precio_unitario': producto.precio
            }
    
    def calcular_total(self):
        subtotal = sum(item['cantidad'] * item['precio_unitario'] for item in self.items.values())
        descuento_total = sum(d.calcular_descuento(subtotal) for d in self.descuentos)
        return max(0, subtotal - descuento_total)

class Orden:
    def __init__(self, usuario, items, direccion_envio):
        self.id = str(uuid.uuid4())
        self.usuario = usuario
        self.items = items
        self.direccion_envio = direccion_envio
        self.fecha_orden = datetime.now()
        self.estado = "pendiente"
        self.total = self.calcular_total()
    
    def calcular_total(self):
        return sum(item['cantidad'] * item['precio_unitario'] for item in self.items.values())
    
    def procesar_pago(self, metodo_pago):
        if metodo_pago.procesar_pago(self.total):
            self.estado = "pagado"
            return True
        return False

class MetodoPago:
    def __init__(self, tipo, detalles):
        self.tipo = tipo
        self.detalles = detalles
    
    def procesar_pago(self, monto):
        return monto > 0
