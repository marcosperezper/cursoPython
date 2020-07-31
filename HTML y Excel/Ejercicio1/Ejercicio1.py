# Leer el fichero "poblacion.xlsx" y cargar los datos en un dataframe
# Con estos datos visualizar cual es la ciudad mas poblada de América

# Leer el fichero "poblacion.csv" y cargar los datos en un dataframe
# Con estos datos visualizar cual es la ciudad mas poblada de América

import pandas as pd

fichero_excel = pd.ExcelFile('HTML y Excel/Ejercicio1/poblacion.xlsx')
excel = fichero_excel.parse('Hoja 1')
# print(excel['Ciudad más poblada'][3])

fichero_csv = pd.read_csv('HTML y Excel/Ejercicio1/poblacion.csv')
print(fichero_csv['Ciudad más poblada'][1])