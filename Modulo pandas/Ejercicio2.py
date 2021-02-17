# Dado el fichero poblacion en varios formatos
# Copiar el fichero al portapapeles
# Crear un dataframe "datos" con esos datos copiados
# Mostrar por pantalla los datos del dataframe
# Mostrar todos los nombre de las columnas del dataframe
# Mostrar la primera fila del dataframe
# Mostrar la primera columna del dataframe
# Mostrar todas las filas pero solo las columnas de "Contiente" y "Poblacion"
# Mostras las 3 primera filas del dataframe
# Mostras las 2 primeras columnas del dataframe

import pandas as pd

dataframe = pd.read_clipboard()

# print(dataframe)
# print(dataframe.columns)
# print(dataframe.loc[0])
# print(dataframe.loc[0:3, ['Continente']])
# print(dataframe.head(3))
print(dataframe.tail(3))