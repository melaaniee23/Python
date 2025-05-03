import math


class Operadores:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,otro):
        return Operadores(self.a+otro.a,self.b+otro.b)
    
    def __sub__(self,otro):
        return Operadores(self.a-otro.a,self.b-otro.b)
    
    def __mul__(self,otro):
        return Operadores(self.a*otro,self.b*otro)
    
    def __truediv__(self,otro):
        return Operadores(self.a/otro.a,self.b/otro.b)
    
    def __floordiv__(self,otro):
        return Operadores(self.a/otro.a,self.b/otro.b)
    
    def __pow__(self,otro):
        return Operadores(self.a**otro.a,self.b**otro.b)
    
    def __mod__(self,otro):
        return Operadores(self.a%otro.a,self.b%otro.b)
    
    def __abs__(self):
        return round(math.sqrt(self.a**2+self.b**2),2)
    
    
    def __str__(self):
        return f"El dato 1 es {self.a} y el dato 2 es {self.b}"
   
    
op1 = Operadores(5,6)
op2 =Operadores(15,24)
suma=op1+op2
print(suma)
resta=op2-op1
print(resta)
multiplicacion=op1*3
print(multiplicacion)
potencia=op2**op1
print(potencia)
divisionEntera=op2/op1
print(divisionEntera)
divisionFlotante=op2/op1
print(divisionFlotante)
modulo=op2%op1
print(modulo)
print(abs(op1))