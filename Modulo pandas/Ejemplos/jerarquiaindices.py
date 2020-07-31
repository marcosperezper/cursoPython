#Jerarquia de indices

import numpy as np
import pandas as pd

lista_valores = np.random.rand(6)
lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
serie = pd.Series(lista_valores,index=lista_indices)

# print(serie[1]['b'])

dataframe = serie.unstack()
# print(dataframe)

lista_valores1 = np.arange(16).reshape(4,4)
lista_indices1 = list('1234')
lista_columnas = list('abcd')
dataframe1 = pd.DataFrame(lista_valores1,index=lista_indices1,columns=lista_columnas)

serie2 = dataframe1.stack()

print(serie2)