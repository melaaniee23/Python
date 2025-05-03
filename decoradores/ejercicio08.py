#clase Producto (nombre,precio), precio atributo privado ,luego hacer un calculo con funcion respectiva , usar validacion 
#comparar nuevos precios , el nuevo precion no puede ser menor de 1 y menor que 1000
#crear def cadena (texto), precio float 
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self._precio = precio
        
    @property
    def precio (self):
       return self._precio
        
    @precio.setter
    def precio(self,nPrecio):
        if nPrecio < 1 or nPrecio > 1000:
            raise ValueError("Precio no valido")
            
        self._precio = nPrecio
        
    @classmethod
    def cadena(cls,texto):
        parte = texto.split("-")    
        nombre =parte[0].strip().title()
        precio=float(parte[1].strip())
        return cls(nombre,precio)
producto =Producto.cadena("Manzana - 80")
print (producto.nombre)
print(producto._precio)

producto.precio=1001
print(producto.precio)