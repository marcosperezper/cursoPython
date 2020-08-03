#Agregacion(operaciones que dan un valor)

import numpy as np
import pandas as pd

lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]
lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores,columns=lista_columnas)
# print(dataframe)

agrupacion1 = dataframe.agg(['sum','min'])
agrupacion2 = dataframe.agg('sum',axis=1)
print(agrupacion2)