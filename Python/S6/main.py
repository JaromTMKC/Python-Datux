from lib.model import UsuarioBd
import sqlite3
from sqlite3 import Connection
def insertData(conn:Connection):
    """nombre=input("ingrese su nombre:")
    edad=input("ingrese su edad:")
    email=input("ingrese su email:")
    user1=UsuarioBd(nombre,edad,email)
    user1.inserInBd(conn)
    """
    user1=UsuarioBd(conn)
    #user1.setData(nombre,edad,email)
    #user1.inserInBd(conn)
    user1.getUsers()
    userBuscar=input("ingrese su usuario a buscar")
    user1.userExist(userBuscar)

if __name__ == '__main__':
    with sqlite3.connect('bdv1.db') as conexion:
        conn=conexion
        insertData(conn)

