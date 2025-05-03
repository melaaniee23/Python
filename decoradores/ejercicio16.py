 #para una clase estudiante que no generara metodos
from dataclasses import dataclass

@dataclass(repr=False)
class Estudiante:
    nombre:str
    edad:int
    
    def __repr__(self):
        return f"nombre={self.nombre}, edad={self.edad}"
        
    
estudiante=Estudiante("Melanie",21)
print(estudiante)

     



    
    