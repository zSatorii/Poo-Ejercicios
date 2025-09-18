class CajaRegistradora:
    def __init__(self, tienda):
        self.tienda = tienda
        self.productos = {}
        self.ventas_dia = {} 
    def agregar_producto(self, producto, precio):
        self.productos[producto] = precio
        self.ventas_dia[producto] = 0
    
    def vender(self, producto, cantidad):
        if producto in self.productos:
            precio_total = self.productos[producto] * cantidad
            self.ventas_dia[producto] += cantidad
            print(f"Venta: {cantidad} {producto} = ${precio_total}")
        else:
            print("Producto no existe")
    
    def mostrar_ventas(self):
        print(f"Ventas del día - {self.tienda}:")
        for producto, cantidad in self.ventas_dia.items():
            total = self.productos[producto] * cantidad
            print(f"{producto}: {cantidad} unidades = ${total}")

caja1 = CajaRegistradora("Tienda El Ahorro")
caja1.agregar_producto("Pan", 2000)
caja1.agregar_producto("Leche", 4500)
caja1.vender("Pan", 3)
caja1.vender("Leche", 2)
caja1.mostrar_ventas()
