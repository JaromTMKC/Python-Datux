from .db import conecta

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

            return totalVentas
        except Exception as e:
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

            return categorias
        except Exception as e:
            print("Error al obtener las categorías:", e)
            return None