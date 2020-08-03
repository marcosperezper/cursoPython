#Renombrar indices

import numpy as np
import pandas as pd

lista_valores = np.arange(9).reshape(3,3)
lista_indices = list('abc')

dataframe = pd.DataFrame(lista_valores, index=lista_indices)

nuevos_indices = dataframe.index.map(str.upper)
dataframe_upper = dataframe.index = nuevos_indices
# print(dataframe)

dataframe = dataframe.rename(index=str.lower)
# print(dataframe)

nuevos_indices1 = {'a':'f','b':'g','c':'h'}
dataframe = dataframe.rename(index=nuevos_indices1)
# print(dataframe)

nuevos_indices2 = {'a':'j','b':'g','c':'h'}
dataframe = dataframe.rename(index=nuevos_indices2,inplace=True)
print(dataframe)
