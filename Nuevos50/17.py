class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def calcular_salario(self):
        raise NotImplementedError("Debe implementar calcular_salario")
    
    def obtener_info(self):
        return f"{self.nombre} {self.apellido}: ${self.calcular_salario():.2f}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_mensual):
        super().__init__(nombre, apellido)
        self.salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, apellido, tarifa_hora, horas_semana):
        super().__init__(nombre, apellido)
        self.tarifa_hora = tarifa_hora
        self.horas_semana = horas_semana
    
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_semana * 4.33  # ~semanas por mes

class EmpleadoPorProyecto(Empleado):
    def __init__(self, nombre, apellido, pago_por_proyecto):
        super().__init__(nombre, apellido)
        self.pago_por_proyecto = pago_por_proyecto
        self.proyectos_completados = 0
    
    def completar_proyecto(self):
        self.proyectos_completados += 1
    
    def calcular_salario(self):
        return self.pago_por_proyecto * self.proyectos_completados