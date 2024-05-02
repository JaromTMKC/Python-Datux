from .db import conecta
from .bitacora import Bitacora

class reporteVentas():
    
    @classmethod
    def generarReporte(self, montoMinimo, categoria):
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "SELECT SUM(actual_price) FROM Ventas"

            condiciones = []
            parametros = []

            if montoMinimo is not None:
                condiciones.append("actual_price >= ?")
                parametros.append(montoMinimo)

            if categoria:
                condiciones.append("category = ?")
                parametros.append(categoria)

            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)

            cursor.execute(query, parametros)
            totalVentas = cursor.fetchone()[0]

            conexion.close()

            Bitacora.log("Acción: generación de reporte exitosa.")
            return totalVentas
        except Exception as e:
            Bitacora.log("Error al generar el reporte de ventas:", e)
            print("Error al generar el reporte de ventas:", e)
            return None
        
    @classmethod 
    def obtenerCategorias(self):
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "SELECT DISTINCT category FROM Ventas"
            cursor.execute(query)

            categorias = [row[0] for row in cursor.fetchall()]

            conexion.close()
            
            Bitacora.log("Acción: Opción 2 elegida")
            Bitacora.log("Acción: Categorías cargadas correctamente")
            return categorias
        except Exception as e:
            Bitacora.log("Error al obtener las categorías:", e)
            print("Error al obtener las categorías:", e)
            return None