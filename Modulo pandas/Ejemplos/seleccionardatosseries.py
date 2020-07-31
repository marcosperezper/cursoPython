#Seleccionar datos en series

import pandas as  pd
import numpy as np 

lista_valores = np.arange(3)
lista_indices = ['i1','i2','i3']

serie = pd.Series(lista_valores, index=lista_indices)

serie = serie * 2
serie[serie > 3] = 6
 
print(serie)