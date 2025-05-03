#crear clase Persona(nombre,edad int),usar dataclass congelado , intentar modificar edad
from dataclasses import dataclass
@dataclass(frozen=True)

class Persona:
   
     nombre:str
     edad:int
     
p=Persona("Melanie",21) 
try:
    p.edad = 31
except AttributeError as e: 
    print(e)
    


