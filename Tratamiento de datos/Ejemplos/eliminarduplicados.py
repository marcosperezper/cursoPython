#Eliminar duplicados en DataFrames

import numpy as np
import pandas as pd

lista_valores = [[1,2],[1,2],[5,6],[5,8]]
lista_indices = list('mnop')
lista_columnas = ['valor1','valor2']

dataframe1 = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
# print(dataframe1)

dataframe2 = dataframe1.drop_duplicates()

dataframe3  = dataframe2.drop_duplicates(['valor1'],keep='last')
print(dataframe3)