class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def mostrarEstudiante(self):
        print(f"El nombre del estudiante es {self.nombre} y tiene {self.edad} años")
        
        
    
estudiante1=Estudiante("Maria","19")
estudiante1.mostrarEstudiante()

        