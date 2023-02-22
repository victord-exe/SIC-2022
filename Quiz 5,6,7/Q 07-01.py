"""
Convierta los siguientes datos del diccionario en un objeto dataframe
usando Pandas. (El objeto del marco de datos se denomina df.)
"""
import pandas as pd


d = {'col1': [1,2], 'col2': [3, 4],
     'col3': [5, 6], 'col4': [7, 8]}

df = pd.DataFrame(list(d.items()))

print(df)