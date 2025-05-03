from dataclasses import dataclass 
@dataclass
class Punto:
    x:int
    y:int 
    
p =Punto(20,30)
print(p)