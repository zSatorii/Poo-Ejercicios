class ProductoCarrito:
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.precio * self.cantidad

class CarritoCompras:
    def __init__(self):
        self.productos = []
        self.descuento_global = 0
    
    def agregar_producto(self, producto):
        # Buscar si ya existe el producto
        for p in self.productos:
            if p.nombre == producto.nombre:
                p.cantidad += producto.cantidad
                return
        self.productos.append(producto)
    
    def quitar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]
    
    def calcular_total(self):
        subtotal = sum(p.subtotal() for p in self.productos)
        return subtotal * (1 - self.descuento_global)
    
    def aplicar_descuento(self, porcentaje):
        self.descuento_global = porcentaje / 100