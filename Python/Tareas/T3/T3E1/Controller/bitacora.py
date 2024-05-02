import datetime

class Bitacora():

    @classmethod
    def log(self, accion):
        try:
            ahora = datetime.datetime.now()
            fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
            
            mensaje = f"[{fecha_hora}] {accion}\n"

            with open('Tareas/T3/T3E1/Static/Assets/bitacora.txt', 'a') as archivo:
                archivo.write(mensaje)
                
            return 0
        except Exception as e:
            print("Error al registrar en la bitácora:", e)
            return -1
    
    @classmethod
    def mostrarBitacora(self):
        try:
            with open('Tareas/T3/T3E1/Static/Assets/bitacora.txt', 'r') as archivo:
                contenido = archivo.read()
                print(contenido)
        except Exception as e:
            print("Error al abrir la bitácora:", e)