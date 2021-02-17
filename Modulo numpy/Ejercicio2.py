# Crear una lista con numeros del 10 al 19
# Crear otra lista con numeros del 50 al 59
# Crear una matriz 2X10 con las listas anteriores
# Crear otra matriz cuyos valores sean iguales a la matriz anterior multiplicados por 2

import numpy as np

lista1 = np.arange(10, 20)
lista2 = np.arange(50, 60)

listadoble = (lista1, lista2)

matriz1 = np.array(listadoble)

matriz2 = matriz1 * 2

print(matriz2)
