#Valores Nulos - NaN

import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4']
serie = pd.Series(lista_valores,index=list('abcd'))
# print(serie.isnull())

seriesinnulos = serie.dropna()
# print(seriesinnulos)

lista_valores1 = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]
lista_indices = list('123')
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores1,index=lista_indices,columns=lista_columnas)
# print(dataframe)
dataframesinnulo = dataframe.dropna()
# print(dataframesinnulo)
dataframarelleno = dataframe.fillna(0)
print(dataframarelleno)