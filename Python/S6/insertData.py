def getInfo():
    name=input("ingrese su nombre")
    correo=input("ingrese su correo")
    return name+";"+correo
with open('./S6/personasv2.txt',mode='+a') as file:
    a=getInfo()
    file.write(a)
    file.close()