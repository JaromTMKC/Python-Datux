#a=10
#print(type(a))

class Celular:
    #definir sus atributos
    marca=None
    ram=None
    almacenamiento=None
    pixeles=None
    precio=None
    def __init__(self,marca,ram,precio):
        # acceder a las variables de mi clase es a la palabra clave self
        self.marca=marca
        self.ram=ram
        self.precio=precio
    def tax(self):
        taxValue=0.18
        self.taxValue=self.precio*taxValue


xiamoi=Celular("xiaomi",64,1200)
#acceder a las variables de mi objecto
print(xiamoi.marca)
xiamoi.tax()
print(xiamoi.taxValue)
samsung=Celular("samsung",128,1800)
samsung.tax()
print(samsung.taxValue)