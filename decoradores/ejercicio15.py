#clase producto (nombre,precio float),usado los operadores de comparacion , tiene que ser una clase ordenada
from dataclasses import dataclass
@dataclass(order=True)
class Producto :
    nombre:str
    precio: float 
    
   
p1 =Producto("Laptop",800 ) 
p2=Producto("Silla",500)
print(p1>p2)   

    