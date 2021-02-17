# Crear dos array con 9 numeros aleatorios entre 0 y 100
# Cambiar el formato de los arrays a una estructura de 3x3
# Crear 2 dataframes de esos arrays
# Concatenar los dos dataframes

import pandas as pd
import numpy as np

array1 = np.random.randint(0, 100, size=9).reshape(3,3)
array2 = np.random.randint(0, 100, size=9).reshape(3,3)

dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)

dataframe_concatenado = pd.concat([dataframe1,dataframe2], ignore_index=True)
print(dataframe_concatenado)