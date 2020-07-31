#Indices
#Indices de dataframes

import pandas as pd 

lista_valores = [1,2,3]
lista_indices = ['a','b','c']

serie = pd.Series(lista_valores, index=lista_indices)


lista_notas = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices1 = ['matematcias','historia','fisica']
lista_nombres = ['Marcos','Do','ThumaDree']

dataframe = pd.DataFrame(lista_notas, index=lista_indices1, columns=lista_nombres)

print(dataframe.values)