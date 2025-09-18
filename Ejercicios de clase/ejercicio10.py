class persona:
    def __new__(cls, nombre, edad):
        return super().__new__(cls)
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __del__(self):
        print("objeto eliminado")
    
ana = persona ("ana", 30)
carlos = persona ("carlos", 47)
print(f"{ana.nombre}, {ana.edad}, {carlos.nombre}, {carlos.edad}")