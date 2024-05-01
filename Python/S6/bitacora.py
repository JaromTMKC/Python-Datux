import datetime

class Log:
    def __init__(self,path):
        self.path=path
        pass

    def formatMessage(self,message):
        now = datetime.datetime.now()
        return f"{now}-{message}"
    def registrar_event(self,message):
        with open(self.path,'+a') as file:
            file.write(message)


l=Log('./ruta')
l.registrar_event('el usuario genero el reporto')