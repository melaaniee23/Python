

import math


class  Operaciones:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __floordiv__(self,otro):
        return self.a / otro.a ,self.b / otro.b
    
    def __mood__(self,otro):
        return self.a % otro.a, self.b % otro.b
    
    def __le__(self,otro):
        return self.a >= otro.a
    
    def __ge__(self,otro):
        return self.a <= otro.a
    
    def __ne__(self,otro):
        return self.a != otro.a
    
    def __lt__(self,otro):
        return self.a > otro.a
   
    def __pow__(self,otro):
        return self.a**otro.a,self.b**otro.b
    
    def __sub__(self,otro):
        return self.a - otro.a, self.b - otro.b
    
    def __bool__(self):
        return self.a > 0
    
    def __abs__(self):
        return round(math.sqrt(self.a**2+self.b**2),2)
    
    def __str__(self):
        return f"Los valores son {self.a},{self.b}"
    
op1 = Operaciones(30,60)
op2 = Operaciones(3,2)

print(op1 >= op2)

print(op1 <= op2)

print(op1 != op2)

print(op1 > op2)

potencia = op1**op2
print(potencia)

resta =op1 - op2
print(resta)


print(abs(op1))

divisionEntera = op1 / op2
print(divisionEntera)

modulo= op1 % op2
print(modulo)