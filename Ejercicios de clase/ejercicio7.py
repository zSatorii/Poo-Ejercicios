class empresa:
    def __init__(self, nombre, empresap, direccion, telefono, empleados):
        self.nombre = nombre
        self.empresap = empresap
        self.direccion = direccion
        self.telefono = telefono
        self.empleados = empleados
empresa1 = empresa("Ramo", "Inversiones SAS", "Calle 123 #13-13", "32030304060", "50 empleados")
print(empresa1.nombre, empresa1.empresap, empresa1.direccion, empresa1.telefono, empresa1.empleados)