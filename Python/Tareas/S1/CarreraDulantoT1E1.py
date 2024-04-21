import os

os.system("cls")

while True:
    os.system("cls")
    respuesta = input("""Este programa en Python te pedirá la siguiente información:
    1) Nombres
    2) Apellidos
    3) DNI
    4) Teléfono
        ¿Deseas continuar? (S/N): """)

    os.system("cls")
    
    if (respuesta.upper() == "S"):
        print("¡Bien!")

        nombre = input("Dime, ¿Cuál es tu nombre?\n")
        os.system("cls")

        apellidos = input("Ahora, ¿Cuál es tu apellido?\n")
        os.system("cls")

        dni = int(input("Luego, ¿Cuál es tu DNI?\n"))
        os.system("cls")

        tel = int(input("Ahora, ¿Cuál es tu número de teléfono?\n"))
        os.system("cls")

        break
    elif(respuesta.upper() == "N"): 
        print("¡Adios!")
        break

os.system("cls")
print(f"""Esta es tu información:\n
      Nombres: {nombre}\n
      Apellidos: {apellidos}\n
      DNI: {dni}\n
      Teléfono: {tel}\n""")