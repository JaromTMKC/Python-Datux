import sqlite3

try:
    def conecta():
        conexion = sqlite3.connect("Tareas/T3/T3E1/database/usuarioDB.db")
        return conexion

    conexion = conecta()

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
except sqlite3.Error as e:
    print("Error al conectar a la base de datos por:\n", e.args[0])