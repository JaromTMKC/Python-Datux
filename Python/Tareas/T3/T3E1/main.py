from Controller.menu import menu
from Controller.usuarioController import usuarioController
from Model.usuario import Usuario
import os

def main():
    os.system("cls")
    
    user = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    usuario = Usuario(0, 0, 0, 0, 0, user, contraseña)
    encontrado = usuarioController.verificarUsuario(usuario)

    if (encontrado != None):
        while True:
            os.system("cls")

            menu.mostrar_menu()
            opcion = input("Seleccione una opción: ")
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

main()