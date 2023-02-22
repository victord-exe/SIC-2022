"""
Escriba un comando para verificar el resumen de
las estadísticas descriptivas (desviación estándar,
valor mínimo, moda, etc.) del marco de datos df
creado en la pregunta 1 e imprima el resultado.
"""
import pandas as pd
from numpy import mean ,median


d = {'col1': [1,2], 'col2': [3, 4],
     'col3': [5, 6], 'col4': [7, 8]}

print("DataFrame original: ")
columnas = ['Primero', 'Segundo']
df = pd.DataFrame(list(d.items()), columns=columnas)


print("")
print("Estadisticas descriptivas del DataFrame")
stats = df.describe(include='all')
print(stats)
