class Precio:
    
    def __new__(cls,precio_Original):
        precio = round(precio_Original)
        print(f"Redondeado €{precio_Original} redondeado a {precio}"  )
       
        instancia =super().__new__(cls)
        instancia.precio=precio
        return instancia        
    
obj1=Precio(17.4)
print(obj1.precio)
        