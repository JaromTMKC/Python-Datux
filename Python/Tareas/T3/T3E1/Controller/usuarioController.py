from .db import conecta
from Model.usuario import Usuario
from .bitacora import Bitacora

class usuarioController():

    @classmethod
    def verificarUsuario(self, usuario):
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "SELECT * FROM Usuario WHERE user_usu = ? AND cont_usu = ?"
            cursor.execute(query, (usuario.user_usu, usuario.cont_usu))
            row = cursor.fetchone()

            if row is not None:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                conexion.close()
                Bitacora.log("Acción: Usuario logueado correctamente")
                return usuario
            else:
                conexion.close()
                Bitacora.log("Acción: Usuario no encontrado, procediendo a crear un nuevo usuario.")
                return None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def registrarUsuario(self, usuario):
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "INSERT INTO Usuario VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6]))

            conexion.commit()
            conexion.close()
            
            Bitacora.log("Acción: Usuario creado correctamente")
            return 0
        except Exception as e:
            Bitacora.log("Error al registrar usuario:", e)
            print("Error al registrar usuario:", e)
            return -1
    
    @classmethod
    def obtenerUltimoID(self):
        conexion = conecta()
        cursor = conexion.cursor()

        query = "SELECT MAX(id_usu) FROM Usuario"
        cursor.execute(query)

        ultimo = cursor.fetchone()[0]

        Bitacora.log("Acción: Retorno de último número de registro correcto.")
        return ultimo

    @classmethod
    def generarID(self, ultimo):
        if ultimo is None:
            nuevo = 1
        else:
            numero = int(ultimo.split('-')[-1])
            
            nuevo = numero + 1
        
        id = f"USR-{nuevo:03d}"
        Bitacora.log("Acción: ID nuevo generado correctamente")
        return id