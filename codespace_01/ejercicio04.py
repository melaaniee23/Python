class Persona:
    def __new__(cls,nombre,edad):
        if edad<18:
            print(f" No se puede crear {nombre}: debe ser mayor de edad, su edad actual es {edad}")
            return None
        
        print(f"Creando persona {nombre} con edad {edad}")
        instancia=super().__new__(cls)
        return instancia

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print(f"La persona {nombre} esta inicializando el programa")
        
p1=Persona("Melanie",18)
print(f"El usuario es : {p1}")

p2=Persona("Nicole",12)
print(f"El usuario es: {p2}")
        