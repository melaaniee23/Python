class MiClase:
    _instancia=None
    
    def __new__(cls,*args,**kwargs):
        if cls._instancia is None:
            print("No existe la instancia")
            print("Creando la instancia")
            cls._instancia=super().__new__(cls)
        else:
            print("La instancia ya esta creada")
        return cls._instancia
    

    def __init__(self,valor):
        self.valor=valor
        
clase1=MiClase("Primero")
clase2=MiClase("Segundo")             

print(clase1.valor)
print(clase2.valor)

print(clase1 is clase2)
print(clase2 is clase1)



                