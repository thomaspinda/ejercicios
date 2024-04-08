class MiClase:
    x=5
p1 = MiClase()
print(p1.x)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

p2 = Persona("Thomas",21)

print(p2.nombre)
print(p2.edad)