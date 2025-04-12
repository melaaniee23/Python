class Libro:
    def __init__(self,titulo,autor,año_publicación):
        self.titulo=titulo
        self.autor=autor
        self.año_publicación=año_publicación
        
    def mostrarLibros(self):
        print(f"El título del libro es {self.titulo}, el autor es {self.autor} y fue publicado en el año {self.año_publicación}")
        
libro1=Libro("El principito","Luis",1980)
libro1.mostrarLibros()