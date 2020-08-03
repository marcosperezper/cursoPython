#Combinaciones de elementos mediante permutacion

import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)

dataframe = pd.DataFrame(lista_valores)

# print(dataframe)

combinacion_aleatoria = np.random.permutation(5)

# print(combinacion_aleatoria)

dataframe_aleatorio = dataframe.take(combinacion_aleatoria)

print(dataframe_aleatorio)