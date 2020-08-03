# Filtrar datos en dataframes 

import pandas as pd
import numpy as np

lista_valores = np.random.rand(10,3)

dataframe = pd.DataFrame(lista_valores)

columna = dataframe[0]

# print(columna[columna > 0.40])

mayores40 = dataframe[dataframe > 0.40 ]
print(mayores40)
#Aqui saca todos los valores del DataFrame pero los que no cumplen la condicion los muestra como NaN