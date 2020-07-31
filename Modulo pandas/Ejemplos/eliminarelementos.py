#Eliminar elementos de series y dataframes

import pandas as pd
import numpy as np

array = np.arange(4)

serie = pd.Series(np.arange(4), index=['a','b','c','d']) 

# print(serie)

seriesinc  =  serie.drop('c')
# print(seriesinc)


lista_valores = np.arange(9).reshape(3,3)
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)

# print(dataframe)

dataframesinb = dataframe.drop('b')

# print(dataframesinb)

dataframesinc2 = dataframesinb.drop('c2',axis=1)

print(dataframesinc2)