#usar dataclass para definir un rectangulo y staticmethod para calcular el area sin crear un objto
from dataclasses import dataclass
@dataclass
class Rectangulo:
    
    base :int
    altura :int
    
    @staticmethod
    def area (b,h):
        return b*h 
    
print(Rectangulo.area(10,20))
rec =Rectangulo(10,20)
print(rec)
