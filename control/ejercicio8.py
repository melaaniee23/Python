class Producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        
producto1=Producto("mochila",50,"utiles escolares")
print(producto1.nombre)
print(producto1.precio)
print(producto1.categoria)        
    