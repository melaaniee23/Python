#crear clase cuenta bancaria,que tenga un atributo saldo,se usa validacion para no permitir menos de 100 y mayor ue 200
# si llega  a ser 100 mandar mesaje diciendo , que su cuenta es menor de 100 y si es 200 mandar mesaje su ceunta es mayoor de 200
# y si llega a ser 150 mandar valuererror,de 100 a 200 mandar mensaje cuenta estable (menos 150)

class CuentaBancaria:
    def __init__(self,saldo):
        self._saldo=saldo
 
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,nSaldo):
        if nSaldo <100 or nSaldo >200:
            raise ValueError("El saldo debe estar entre los 100 y 200")
            
        
        if nSaldo == 99 :
            print("La cuenta es menor que 100")
        elif nSaldo ==201:
            print("La cuenta es mayor que 200")
        elif nSaldo ==150:
            raise ValueError("No se permite el saldo de 150")
        else:
            print("La cuenta es estable")
            
        self._saldo =nSaldo
    
cb = CuentaBancaria(201)
cb.saldo =100
print(cb.saldo)

        
   
    
   
    
 
    
    
    