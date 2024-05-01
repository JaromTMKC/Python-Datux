def getInfo():
    name=input("ingrese su nombre")
    correo=input("ingrese su correo")
    return name+";"+correo
with open('./modulo4/personasv2.txt',mode='+a') as file:
    a=getInfo()
    file.write(a)
    file.close()