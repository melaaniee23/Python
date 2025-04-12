class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        
    def imprimirSaldo(self):
        print(f"El saldo actual es de {self.saldo}  y el titular es {self.titular}")
        
cB=CuentaBancaria("Maria",1290)
cB.imprimirSaldo()