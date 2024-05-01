#apuntes base de datos
# consultas , insercciones y actualizaciones => querys
#  agrupar la logica => store procedures 
import sqlite3

conexion = sqlite3.connect('bdv1.db')
cursor = conexion.cursor()
sentencia = """
CREATE TABLE IF NOT EXISTS usuarios(
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
)
"""
cursor.execute(sentencia)

sentencia2 = """
INSERT INTO usuarios VALUES
('Hector', 27, 'hector@ejemplo.com')
"""
cursor.execute(sentencia2)
conexion.commit()

conexion.close()