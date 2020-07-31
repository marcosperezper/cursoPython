#Ordenar y clasificar series

import pandas as  pd
import numpy as np

lista_valores = range(4)
lista_indices = list('CABD')

serie = pd.Series(lista_valores, index=lista_indices)

serie_ordenadai = serie.sort_index()
# print(serie_ordenadai)
serie_ordenadav = serie.sort_values()
# print(serie_ordenadav)

ranking = serie.rank()
# print(ranking)

serie2 = pd.Series(np.random.randn(10))
# print(serie2)

ranking2= serie2.rank()
print(ranking2)