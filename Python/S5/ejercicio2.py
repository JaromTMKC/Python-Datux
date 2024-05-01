# realice una funcion que pida numeros e insertelos en una lista , y luego imprimir la division del numero i-1 y i
# capturar error
while True:
    msg="""
        1.Ingresar un nuevo numero
        2.salir
    """
    print(msg)
    opcion= int(input("ingresa una opcion"))
    if opcion == 1:
        lista=[]
        while True:
            denominador_init=1
            try:
                numero=int(input("ingresa un numero"))
                lista.append(numero)
                index=lista.index(numero)
                print('index',index)
                if len(lista)>=2:
                    print("here")
                    print(lista[index]/lista[index-1]) 
                else:
                    print("else")
                    print(lista[index]/denominador_init)
            except:
                print(lista)
                pass
                print("error al ingresar un numero")
    
    if opcion == 2:
        break