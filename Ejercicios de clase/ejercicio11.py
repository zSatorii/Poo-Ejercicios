class producto:
    print("Esta clase es nueva")

    def _init_(self, producto, precio):
        self.precio = precio
        self.producto = producto

    def _str_(self):
        return f"{self.producto}, {self.precio}"

    def _repr_(self):
        return f"{self.producto}, {self.precio}"

    def _format_(self, formato):
        if formato == "precio":
            return f"{self.precio}"
        return str(self)

var = producto("computador", 3000000)

print(var)             
print(repr(var))       
print(f"{var.precio}")