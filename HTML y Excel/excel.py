#Fichero formato Excel

import pandas as pd


fichero_excel = pd.ExcelFile('HTML y Excel/ficheroexcel.xlsx')
dataframe = fichero_excel.parse('Hoja1')

print(dataframe)