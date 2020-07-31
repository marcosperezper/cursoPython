#Operaciones en series y dataframes

import pandas as  pd
import numpy as np 

serie1 = pd.Series([0,1,2],index=['i1','i2','i3'])
# print(serie1)
serie2 = pd.Series([3,4,5,6,],index=['i1','i2','i3','i4'])

sumas_series = serie1 + serie2

# print(sumas_series)

lista_valores = np.arange(4).reshape(2,2)
lista_indices = list('ab')
lista_columnas = list('12')
dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)

lista_valores2 = np.arange(9).reshape(3,3)
lista_indices2 = list('abc')
lista_columnas2 = list('123')
dataframe2= pd.DataFrame(lista_valores2,index=lista_indices2,columns=lista_columnas2)

suma_dataframe = dataframe + dataframe2

print(dataframe.add(dataframe2,fill_value=0))
