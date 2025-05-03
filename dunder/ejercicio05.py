import math


class Operaciones:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    
    def __mul__(self,otro):
        return self.a*otro.a,self.b*otro.b
    
    def __neg__(self):
        return Operaciones(-self.a,self.b)
    
    def __abs__(self):
        return round(math.sqrt(self.a**2+self.b**2),2)
    
    def __add__(self,otro):
        return self.a+otro.a,self.b+otro.a
    
    def __truediv__(self,otro):
        return self.a/otro.a,self.b/otro.a
    
    def __str__(self):
        return f"Los valores son {self.a},{self.b}"
    
op =Operaciones(20,10)
op1=Operaciones(5,2)
multiplicacion=op*op1
print(multiplicacion)

negacion= -op
print(negacion)

valorAbsoluto=op
print(abs(op))

suma=op+op1
print(suma)

divisionFlotante=op/op1
print(divisionFlotante)