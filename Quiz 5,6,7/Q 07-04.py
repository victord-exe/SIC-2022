"""
Escriba un comando para buscar datos faltantes
en el dataframe df creado en la Pregunta 1 e imprima
el resultado. (Sin embargo, los datos que faltan
deben devolverse como verdaderos).

"""

import pandas as pd


d = {'col1': [1,2], 'col2': [3, 4],
     'col3': [5, 6], 'col4': [7, 8]}

df = pd.DataFrame(list(d.items()))


print (df)

print(pd.isna(df))