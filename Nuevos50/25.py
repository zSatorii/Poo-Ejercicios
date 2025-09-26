class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

class Producto:
    def __init__(self, nombre, precio, stock, categoria=None):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        if categoria:
            categoria.productos.append(self)
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
    
    def esta_disponible(self):
        return self.stock > 0

class Inventario:
    def __init__(self):
        self.productos = {}
        self.categorias = {}
    
    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto
    
    def buscar_producto(self, nombre):
        return self.productos.get(nombre)
    
    def productos_por_categoria(self, nombre_categoria):
        if nombre_categoria in self.categorias:
            return self.categorias[nombre_categoria].productos
        return []
    
    def valor_total_inventario(self):
        return sum(p.precio * p.stock for p in self.productos.values())
