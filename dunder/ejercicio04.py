class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def __eq__(self, otros):
        return self.edad == otros.edad
    
    def __ne__(self,otros):
        return self.edad != otros.edad
    
    def __lt__(self,otros):
        return self.edad > otros.edad
    
    def __le__(self,otros):
        return self.edad >= otros.edad
    
    def __gt__(self,otros):
        return self.edad < otros.edad
    
    def __ge__(self,otros):
        return self.edad <= otros.edad
    
    def __bool__(self):
        return self.edad>20 and bool(self.nombre) 
    
    
p1=Persona("Melanie",20)
p2=Persona("Luis",20)
p3=Persona("Melanie",22)

print(p1==p2)
print(p1 > p2)
print(p1 >= p2)
print(p1 < p2)
print(p1 <= p2)
print(f"Este es un metodo de valores logicos {bool(p1)}")
print(f"Este es otro metodo de valores logicos {bool(p3)}")