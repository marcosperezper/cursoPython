#Series
import pandas as pd

serie1 = pd.Series([3,5,7])

# print(serie1)

asignaturas = ['matematicas','fisica','historia','literatura']
notas = [8,6,9,7]

serie_notas_marcos = pd.Series(notas,index=asignaturas) 

# print(serie_notas_marcos)


diccionario = serie_notas_marcos.to_dict()

# print(diccionario)

serie = pd.Series(diccionario)

# print(serie)

notas_ana = [5,4,9,10]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)

# print(serie_notas_ana)

serie_notas_clase = (serie_notas_ana + serie_notas_marcos) / 2

print(serie_notas_clase)