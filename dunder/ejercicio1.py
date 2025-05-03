class Persona:
    
    def __new__(cls,*args,**Kwargs):
        return super().__new__(cls)
    
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def __del__ (self):
        print(f"{self.nombre} ha sido eliminado.")
        
persona1 = Persona("Pablo",19)
persona2 = Persona("Carmen",25)
del persona2
persona3 = Persona("Maria",46)



print(f"{persona1.nombre}  sigue vivo")
print(f"{persona3.nombre}  sigue vivo")

input("Presiona enter si quieres terminar el programa")

