class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
        
class Perro(Animal):
     def __init__(self,raza,nombre):
        super().__init__(nombre)
        self.raza=raza
        
   
         
perro1=Perro("Max","Pomerania")
print(perro1.nombre)
print(perro1.raza)
