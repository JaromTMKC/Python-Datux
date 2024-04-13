import os

os.system("cls")

opcion = input("""El siguiente programa le hará saber a que tipo de tarjeta de crédito es acreedor según ciertos datos que se le pedirá.
      ¿Desea continuar?(S/N):  """)

os.system("cls")

while True:
    if (opcion.upper() == "S"):
        os.system("cls")
        edad = int(input("Primero, ¿Cuál es tu edad?: "))

        if (edad < 18):
            os.system("cls")
            print("Lo siento, no puedes seguir, aún no eres mayor de edad :c")
            break
        else:
            ingreso = float(input("Bien, ¿Cuál es tu ingreso mensual?: "))

            if (ingreso < 1000):
                os.system("cls")
                print("Lo siento, no puedes seguir, tu sueldo no abastece la obtención de una tarjeta de crédito :c")
                break
            else:
                os.system("cls")

                if (ingreso > 1000 and ingreso < 3000) :
                    print("Usted puede solicitar una tarjeta de crédito 'CLÁSICA'")
                else:
                    print("Usted puede solicitar una tarjeta de crédito 'DORADA'")
        op = input("¿Desea continuar?(S/N): ")

        if (op.upper() != "S"):
            os.system("cls")
            print("Adios!")
            break
    
    elif opcion.upper() == "N":
        os.system("cls")
        print("¡Adiós!")
        break