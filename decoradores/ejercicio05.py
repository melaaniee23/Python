class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
        
    @classmethod
    def cadena (cls,texto):
        nombre = texto.strip().title()
        return cls(nombre)
    
p =Persona.cadena("Melanie")
print(p.nombre)
        
        