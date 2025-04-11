from dataclasses import dataclass
@dataclass(Frozen=True)

class MiClase:
    nombre:str
    duracion:int
  
    def __init__(self,nombre, duracion):
        self.nombre= nombre
        self.duracion=duracion
        
    def mostrarClase(self):
        print(f"La clase de {self.nombre} y dura {self.duracion} horas")
        
        
    
clase1=MiClase("Python",2)
clase1.mostrarClase()
  

    