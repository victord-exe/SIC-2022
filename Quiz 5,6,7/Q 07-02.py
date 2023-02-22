"""
Para el dataframe creado en la Pregunta 1,
cree un nuevo dataframe que consista
sólo en los datos de la columna con el nombre
de columna 'col4'. (El dataframe se denomina new_df.)
"""

import pandas as pd


d = {'col1': [1,2], 'col2': [3, 4],
     'col3': [5, 6], 'col4': [7, 8]}

df = pd.DataFrame(list(d.items()))

new_df = df.iloc[3, 1]

print (new_df)