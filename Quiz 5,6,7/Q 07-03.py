"""
El índice del dataframe creado en la Pregunta 1 es 0,1.
Escriba un comando para cambiar el nombre de estos
índices a primero y segundo."""

import pandas as pd


d = {'col1': [1,2], 'col2': [3, 4],
     'col3': [5, 6], 'col4': [7, 8]}

columnas = [1, 2]
df = pd.DataFrame(list(d.items()), columns=columnas)

print(df)
print("")
columnas = ['Primero', 'Segundo']
df = pd.DataFrame(list(d.items()), columns=columnas)

print(df)