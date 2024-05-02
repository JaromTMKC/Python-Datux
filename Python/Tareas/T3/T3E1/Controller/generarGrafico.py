from .db import conecta
import matplotlib.pyplot as plt
import pandas as pd

class generarGrafico():
    @staticmethod
    def generar():
        try:
            conexion = conecta()
            cursor = conexion.cursor()

            query = "SELECT category, SUM(actual_price) AS total_ventas FROM Ventas GROUP BY category ORDER BY total_ventas DESC LIMIT 10"
            cursor.execute(query)
            resultados = cursor.fetchall()

            df = pd.DataFrame(resultados, columns=['Categoría', 'Total Ventas'])

            plt.figure(figsize=(10, 6))
            plt.bar(df['Categoría'], df['Total Ventas'], color='skyblue')
            plt.title('Total de Ventas por Categoría (Top 10)')
            plt.xlabel('Categoría')
            plt.ylabel('Total de Ventas')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

            conexion.close()
            
            return 0
        except Exception as e:
            print("Error al generar el gráfico de ventas por categoría:", e)