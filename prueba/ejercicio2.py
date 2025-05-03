class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor=autor
        
    @property
    def titulo (self):
        return self.titulo
    
    @titulo.setter
    def titulo(self,nTitulo):
        if nTitulo ==" ":
            raise ValueError("El titulo no puede estar vacio")
        
    @classmethod
    def cadena (cls,texto):
        parte =texto.split(',')
        titulo =parte[0].strip().title()
        autor =parte[1].strip().title()
        return cls(titulo,autor)
    
    @staticmethod
    def tiempoLecturra(paginas, minutos):
        return paginas*minutos
    
libro =Libro 
    
            