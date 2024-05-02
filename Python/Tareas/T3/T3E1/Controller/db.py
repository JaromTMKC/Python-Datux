import sqlite3
from .bitacora import Bitacora

try:
    def conecta():
        conexion = sqlite3.connect("Tareas/T3/T3E1/database/usuarioDB.db")
        return conexion
    
    Bitacora.log("Acción: Intento de conexión a la BD")

    conexion = conecta()

    Bitacora.log("Acción: Conexión a la BD realizada")

    cursor = conexion.cursor()
    query = """CREATE TABLE IF NOT EXISTS Usuario(
            id_usu VARCHAR(250) PRIMARY KEY,
            nomb_usu VARCHAR(80),
            apel_usu VARCHAR(80),
            dni_usu CHAR(8),
            tele_usu CHAR(9),
            user_usu VARCHAR(250),
            cont_usu VARCHAR(250)
    )"""

    cursor.execute(query)

    conexion.commit()
    conexion.close()

    Bitacora.log("Acción: Creación de tabla Usuario")
except sqlite3.Error as e:
    Bitacora.log("Error al conectar a la base de datos por:\n", e.args[0])