import os

os.system("cls")

opcion = input("""El siguiente programa sumará automaticamente los números anteriores al que usted digite hasta el número en cuestión.
      ¿Desea continuar?(S/N):  """)

os.system("cls")

while True:
    if (opcion.upper() == "S"):
        numero = int(input("Dígite el número: "))
        suma = 0

        for i in range(1, numero + 1):
            suma = suma + i
        break

    elif opcion.upper() == "N":
        os.system("cls")
        print("¡Adiós!")
        break


print(f"La suma de números desde el 1 hasta el {numero} es: ", suma)