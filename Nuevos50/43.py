class ProductoInteligente:
    def __init__(self, codigo, nombre, precio, stock_actual, stock_minimo, stock_maximo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.historial_movimientos = []
        self.demanda_promedio = 0
        self.lead_time = 7  # días
    
    def registrar_movimiento(self, tipo, cantidad, motivo=""):
        movimiento = {
            'tipo': tipo,  # entrada, salida
            'cantidad': cantidad,
            'fecha': datetime.now(),
            'motivo': motivo,
            'stock_antes': self.stock_actual
        }
        
        if tipo == "salida":
            self.stock_actual -= cantidad
        elif tipo == "entrada":
            self.stock_actual += cantidad
            
        movimiento['stock_despues'] = self.stock_actual
        self.historial_movimientos.append(movimiento)
    
    def calcular_demanda_promedio(self):
        # Calcular demanda de los últimos 30 días
        hace_30_dias = datetime.now() - timedelta(days=30)
        salidas_recientes = [
            m for m in self.historial_movimientos 
            if m['tipo'] == 'salida' and m['fecha'] >= hace_30_dias
        ]
        
        if salidas_recientes:
            total_vendido = sum(m['cantidad'] for m in salidas_recientes)
            self.demanda_promedio = total_vendido / 30
        
        return self.demanda_promedio

class Proveedor:
    def __init__(self, nombre, contacto, tiempo_entrega, calificacion=5):
        self.nombre = nombre
        self.contacto = contacto
        self.tiempo_entrega = tiempo_entrega
        self.calificacion = calificacion
        self.productos_suministrados = []
        self.ordenes_completadas = 0

class OrdenCompra:
    def __init__(self, proveedor, productos_solicitados):
        self.id = str(uuid.uuid4())
        self.proveedor = proveedor
        self.productos_solicitados = productos_solicitados  # {producto: cantidad}
        self.fecha_orden = datetime.now()
        self.fecha_entrega_esperada = datetime.now() + timedelta(days=proveedor.tiempo_entrega)
        self.estado = "pendiente"
        self.total = self.calcular_total()
    
    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos_solicitados.items())
    
    def marcar_recibida(self):
        self.estado = "recibida"
        for producto, cantidad in self.productos_solicitados.items():
            producto.registrar_movimiento("entrada", cantidad, f"Orden {self.id}")

class SistemaInventarioInteligente:
    def __init__(self):
        self.productos = {}
        self.proveedores = {}
        self.ordenes_compra = []
        self.alertas = []
    
    def verificar_restock_necesario(self):
        productos_restock = []
        for producto in self.productos.values():
            producto.calcular_demanda_promedio()
            
            # Punto de reorden = demanda_promedio * lead_time + stock_seguridad
            stock_seguridad = producto.stock_minimo
            punto_reorden = (producto.demanda_promedio * producto.lead_time) + stock_seguridad
            
            if producto.stock_actual <= punto_reorden:
                productos_restock.append(producto)
                
                alerta = f"Producto {producto.nombre} necesita restock. Stock actual: {producto.stock_actual}"
                self.alertas.append(alerta)
        
        return productos_restock
    
    def generar_orden_automatica(self, producto, proveedor):
        cantidad_optima = producto.stock_maximo - producto.stock_actual
        orden = OrdenCompra(proveedor, {producto: cantidad_optima})
        self.ordenes_compra.append(orden)
        return orden
    
    def analisis_abc(self):
        # Clasificación ABC basada en valor de inventario
        productos_valor = []
        for producto in self.productos.values():
            valor_inventario = producto.precio * producto.stock_actual
            productos_valor.append((producto, valor_inventario))
        
        productos_valor.sort(key=lambda x: x[1], reverse=True)
        
        total_valor = sum(valor for _, valor in productos_valor)
        acumulado = 0
        clasificacion = {}
        
        for producto, valor in productos_valor:
            acumulado += valor
            porcentaje_acumulado = (acumulado / total_valor) * 100
            
            if porcentaje_acumulado <= 80:
                clasificacion[producto.codigo] = 'A'
            elif porcentaje_acumulado <= 95:
                clasificacion[producto.codigo] = 'B'
            else:
                clasificacion[producto.codigo] = 'C'
        
        return clasificacion
