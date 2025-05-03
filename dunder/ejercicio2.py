class Persona:
    
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self):
        return f"La persona se llama {self.nombre} y su edad es {self.edad}"
    
    def __repr__(self):
        return f"{self.nombre} tiene la edad {self.edad}"
p1 = Persona("Melanie",18)
print(p1)
print(str(p1))
print(repr(p1))
        
    