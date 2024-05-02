from Controller.menu import menu
from Controller.usuarioController import usuarioController
from Model.usuario import Usuario
from Controller.generarIngresoCSV import generacion
from Controller.reporteCSV import reporteVentas
from Controller.generarGrafico import generarGrafico

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
            elif opcion == '2':
                os.system("cls")

                print("Ahora se mostrará en pantalla las caregorías por la cuales podrá filtrar el reporte (en base a esa categoría se generará el reporte).")
                time.sleep(1.8)
                os.system("cls")

                categorias = reporteVentas.obtenerCategorias()
                if categorias:
                    print("-----Categorías-----\n")
                    for categoria in categorias:
                        print(categoria, "\n")
                    
                    cat = input("¿En base a qué categoría quiere filtrar el reporte?\n")
                    
                    os.system("cls")
                    
                    montoMinimo = float(input("¿Cuál será el monto mínimo a tomar en cuenta (precio del producto)?\n"))
                    
                    salidaReporte = reporteVentas.generarReporte(montoMinimo, cat)
                    
                    if salidaReporte is not None:
                        os.system("cls")
                        print(f"Total de ventas filtradas por categoria '{cat}', monto mínimo '{montoMinimo}\n      ${salidaReporte}")
                    else:
                        print("No se pudo generar el reporte de ventas.")

                    time.sleep(3.5)
                    os.system("cls")
                else :
                    os.system("cls")
                    print("No se olvide primero de usar la opción 1 del menú!")
                    time.sleep(1.5)
            elif opcion == '3':
                print("En esta opción se generará un gráfico de barras en correlación del total de ventas de cada categoría.")
                os.system("cls")

                respuestaGrafico = reporteVentas.obtenerCategorias()
                os.system("cls")

                if respuestaGrafico:
                    generarGrafico.generar()
                else:
                    os.system("cls")
                    print("No se olvide primero de usar la opción 1 del menú!")
                    time.sleep(1.5)
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