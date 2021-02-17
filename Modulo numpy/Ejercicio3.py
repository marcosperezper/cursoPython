# Crear una lista con los valores numericos del 0 al 30
# Crear otra lista con los primeros 10 valores de la lista inicial
# Crear otra con los ultimos 10 valores de la lista inicial
# Crear un bucle que recorra esta ultima lista de valores finales


import numpy as np


lista = np.arange(0,30)

principio = lista[1:10]
final = lista[-10:]

for numero in final:
    print(numero)