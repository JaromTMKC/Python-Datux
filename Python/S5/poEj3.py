# las clases se pueden generalizar osea puedo crear una clase padre y luego hacer un clase hijo , 
# la clase hijo va a heredar todo del padre

class Celuar:
    def __init__(self,ram:int,procesador:str,display:str,camara:dict) -> None:
        self.isConfig=False
        self.config:dict={
            'name':'',
            'correo':'',
            'verficado':False
        }
        self.procesador=procesador
        self.display=display
        self.camara=camara
        self.ram=ram

    def setConfig(self):
        if not self.isConfig :
           name=input("ingrese nombre de usuario:")
           correo=input("ingrese tu correo electronico: ")
           self.config['name']=name
           self.config['correo']=correo
        else:
            print(f"El dispositivo esta configurado {self.config['name']} y {self.config['correo']}")
    def verConfig(self):
         print(f"El dispositivo esta configurado  {self.config['name']} y {self.config['correo']}")

class Xiamoi(Celuar):
    def setConfig(self):
        print("nueva configuracion")
        return super().setConfig()
    def verConfig(self):
        print(f"El dispositivo xiaomi esta configurado  {self.config['name']} y {self.config['correo']}")



c1=Celuar(4,"ryzon 8gb","3x4",{'frontal':14,'trasera':15})
#c1.setConfig()
#c1.verConfig()
xia=Xiamoi(4,"ryzon 8gb","3x4",{'frontal':14,'trasera':15})
xia.setConfig()
xia.verConfig()