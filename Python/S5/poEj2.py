class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)
    def __str__(self):
        #return "hola yo sobreescribo la impresion de la direccion de memoria (<__main__.Pelicula object at 0x7f8dc228bdf0> )"
        return f"la pelicula es {self.titulo} del año {self.lanzamiento}"
    """ 
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento) """
class Catalogo:
    peliculas = []
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)
    def mostrar(self):
        print("mostrando catalogo")
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

p = Pelicula("El Padrino", 175, 1972)
c1=Catalogo([p])
c1.mostrar()