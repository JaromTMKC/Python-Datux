import os

pathv2=os.path.abspath('.')
print(pathv2)
def mostrarListaDocumentos(path):
    lista=os.listdir(path)
    for i in lista:
        ruta_nueva=os.path.join(path,i)
        if os.path.isdir(ruta_nueva):
            mostrarListaDocumentos(ruta_nueva)
        if os.path.isfile(ruta_nueva):
            print(ruta_nueva)

try:
    mostrarListaDocumentos(pathv2)
except Exception as error:
    print("error",error)