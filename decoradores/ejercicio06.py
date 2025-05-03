class Libro:
    def __init__(self,titulo,autor):
        self.titulo =titulo
        self.autor =autor
        
    @classmethod
    def cadena (cls,texto):
        parte =texto.split(',')
        titulo = parte[0].strip().title()
        autor =parte[1].strip().title()
        return cls(titulo,autor)
    
libro =Libro.cadena("A 2 metros de tí  Gabriel García")
print(libro.titulo)
print(libro.autor)
