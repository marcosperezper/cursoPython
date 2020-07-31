#Estadisticas en dataframes

import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])

dataframe = pd.DataFrame(array, index=['a','b'],columns=list('123'))

# print(dataframe)

suma_columnas = dataframe.sum()
# print(suma_columnas)
suma_filas = dataframe.sum(axis=1)
# print(suma_filas)

minimo = dataframe.min()
# print(minimo)

maximo = dataframe.max(axis=1)
# print(maximo)

indicemin = dataframe.idxmin()
# print(indicemin)

print(dataframe.describe())
