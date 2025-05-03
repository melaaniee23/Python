class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    @property
    def area(self):
        return 0.5*self.base*self.altura
        
    
t =Triangulo(10,20)
print(t.area)        
        