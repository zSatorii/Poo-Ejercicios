class ClasificadorProductos:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.descuento = 0
    
    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje
    
    def clasificar_por_precio(self):
        precio_final = self.precio - (self.precio * self.descuento / 100)
        print(f"Producto: {self.nombre}")
        print(f"Precio original: ${self.precio}")
        print(f"Precio final: ${precio_final}")
        
        if precio_final < 50000:
            print("Clasificación: ECONÓMICO")
        if precio_final >= 50000 and precio_final < 200000:
            print("Clasificación: MEDIO")
        if precio_final >= 200000 and precio_final < 500000:
            print("Clasificación: CARO")
        if precio_final >= 500000:
            print("Clasificación: PREMIUM")
    
    def recomendar_publico(self):
        if self.categoria == "electronico":
            print("Público objetivo: Tecnólogos y gamers")
        if self.categoria == "ropa":
            print("Público objetivo: Jóvenes y adultos")
        if self.categoria == "hogar":
            print("Público objetivo: Familias")
        if self.categoria == "deportes":
            print("Público objetivo: Deportistas")

# Uso
producto1 = ClasificadorProductos("Smartphone", 800000, "electronico")
producto1.aplicar_descuento(10)
producto1.clasificar_por_precio()
producto1.recomendar_publico()

