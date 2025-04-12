class Coche:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        
    def mostrarCoche(self):
        print(F"La marca del coche es {self.marca} y el modelo es un {self.modelo}")
        
coche1=Coche("Toyota","clio")
coche1.mostrarCoche()
        