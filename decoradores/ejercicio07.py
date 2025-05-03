#clase Estudiante(nombre,edad,carrera),metodo de clase que reciba una cadena con el formato "-"
class Estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad =int (edad)
        self.carrera = carrera
        
    @classmethod
    def cadena (cls,texto):
        parte = texto.split('-')
        nombre = parte[0].strip().title()
        edad = parte[1].strip()
        carrera=parte[2].strip().title()
        return cls(nombre,edad,carrera)
    
est =Estudiante.cadena("Luis ´- 19 - Ingenieria")
print(est.nombre)
print(est.edad)
print(est.carrera)
        
        
