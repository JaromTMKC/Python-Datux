import os

os.system("cls")

opcion = input("""El siguiente programa le mostrará en consola el tipo de dato de cualquier variable que se le pedirá a continuación.
      ¿Desea continuar?(S/N):  """)

os.system("cls")

while True:
    if opcion.upper() == "S":
        os.system("cls")
        clave = input("""Digite cualquier cosa: 
                      'Psst... Pueden ser números, letras o decimales'\n""")

        if clave.isdigit():
            print("El tipo de dato que escribió corresponde a: int")
        else:
            try:
                float(clave)
                print("El tipo de dato que escribió corresponde a: float (decimal)")
            except ValueError:
                print("El tipo de dato que escribió corresponde a: string (cadena)")
        
        op = input("¿Desea continuar? (S/N)")
        os.system("cls")
    
        if op.upper() != "S":
            os.system("cls")
            print("¡Adiós!")
            break

    elif opcion.upper() == "N":
        os.system("cls")
        print("¡Adiós!")
        break
