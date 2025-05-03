class CuentaBancaria:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self._saldo=saldo
        
    @property
    def saldo (self):
        return self._saldo
    
    @saldo.setter
    def saldo (self,nSaldo):
        if nSaldo < 0:
            raise ValueError("Saldo invalido")
        
    @classmethod
    def cadena (cls,texto):
        partes =texto.split(',')
        nombre =partes[0].strip().title()
        saldo = int (partes[1].strip())
        return cls(nombre,saldo)
    
cb =CuentaBancaria("Melanie",200)
print(cb.nombre)
print(cb.saldo)
        