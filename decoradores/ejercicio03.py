class Producto:
    def __init__(self,precio):
        self._precio=precio
        
    @property    
    def precio (self):
     return self._precio
 
    @precio.setter
    def precio(self,nPrecio):
        if nPrecio < 0 :
            raise ValueError("No se aceptan precios negativos")
       
        self._precio = nPrecio
        
        
p =Producto(100)
p.precio=-1
print(p.precio)


