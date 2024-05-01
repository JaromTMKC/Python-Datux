from Controller.menu import menu
from Controller.usuarioController import usuarioController
from Model.usuario import Usuario
from Controller.generarIngresoCSV import generacion

import os
import time

def main():
    os.system("cls")
    
    user = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    usuario = Usuario(0, 0, 0, 0, 0, user, contraseña)
    encontrado = usuarioController.verificarUsuario(usuario)

    if (encontrado != None):
        while True:
            os.system("cls")
            
            print(f"Bienvenid@ {usuario.user_usu}!\n\n")
            menu.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                os.system("cls")

                print("Ahora se ejecutará una acción automatizada para el ingreso de un archivo csv a la bd.")
                time.sleep(3)
                salidaGen = generacion.insertar()

                if salidaGen == 0:
                    time.sleep(1.5)
            #elif opcion == '2':
                # Opción 2: Generar reporte de ventas
                #import generar_reporte
                #generar_reporte.generar_reporte_ventas()
            #elif opcion == '3':
                # Opción 3: Generar gráfico de ventas
                #import generar_grafico
                #generar_grafico.generar_grafico_ventas()
            #elif opcion == '4':
                # Opción 4: Generar bitácora
                #import bitacora
                #bitacora.crear_bitacora()
            elif opcion == '5':
                generacion.eliminación()
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    else :
        os.system("cls")
        print("Al parecer no estás registrado...\nDame los datos que te pediré para registrarte.\n")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        User = input("Usuario: ")
        cont = input("Contraseña: ")

        ultimo = usuarioController.obtenerUltimoID()
        id = usuarioController.generarID(ultimo)

        usuarioNuevo = [id, nombre, apellido, dni, telefono, User, cont]
        respuesta = usuarioController.registrarUsuario(usuarioNuevo)

        if (respuesta == 0):
            print("Registrado correctamente")
        else:
            print("Error al registrar usuario. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    main()