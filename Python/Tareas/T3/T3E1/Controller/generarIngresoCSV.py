import csv
from .db import conecta
from .bitacora import Bitacora

class generacion():
    
    @classmethod
    def insertar(cls):
        try:
            with open("Tareas/T3/T3E1/Static/Assets/amazon.csv", 'r', newline='', encoding='utf-8') as CSV:
                lectorCSV = csv.reader(CSV)
                nombresColumnas = next(lectorCSV)

            conexion = conecta()
            cursor = conexion.cursor()

            query = f"CREATE TABLE IF NOT EXISTS Ventas ({', '.join(nombresColumnas)})"
            cursor.execute(query)

            with open("Tareas/T3/T3E1/Static/Assets/amazon.csv", 'r', newline='', encoding='utf-8') as CSV:
                next(CSV)  
                lectorCSV = csv.reader(CSV)

                for fila in lectorCSV:
                    fila_filtrada = [valor.replace("₹", "") for valor in fila]
                    
                    query2 = f"INSERT INTO Ventas VALUES ({', '.join(['?' for _ in range(len(fila))])})"
                    cursor.execute(query2, fila_filtrada)

            conexion.commit()
            conexion.close()

            print("Generación Exitosa!")
            Bitacora.log("Acción: Opción 1 elegida")
            Bitacora.log("Acción: Inserción de datos a la tabla Ventas correcta")
            return 0
        except Exception as e:
            Bitacora.log("Error en inserción de datos:", e)

    @classmethod
    def eliminación(self):
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "DELETE FROM Ventas"
            cursor.execute(query)

            conexion.commit()
            conexion.close()

            Bitacora.log("Acción: Eliminación de datos en la tabla Ventas correcta")
        except Exception as e:
            Bitacora.log("Error al eliminar registros", e)