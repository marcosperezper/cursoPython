# Vamos a filtrar datos en un DataFrame.

# Crearemos una lista con 50 valores aleatorios entre los valores 0 y 100
# Convertiremos esta lista en un dataframe con 5 filas y 10 columnas
# Filtraremos los datos del dataframe para visualizar solo los valores mayores de 50 

import pandas as pd
import numpy as np

lista_valores =  np.random.randint(0,100,size=50).reshape(5,10)
dataframe = pd.DataFrame(lista_valores)

mayores_de_50 = dataframe[dataframe > 50]

print(mayores_de_50)