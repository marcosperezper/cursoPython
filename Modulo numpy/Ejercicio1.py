# Crear la funcion "pares" que devuelva un array de numeros pares entre dos valores pasados como parametro a la funcion (inicio y fin)
# Utilizar la funcion con los numeros 1 y 30
# Utilizar la funcion con los numeros 2 y 40

import numpy as np

def pares(inicio, fin):
    if(inicio % 2 == 0):
         array = np.arange(inicio,fin,2)
    else:
        inicio = inicio + 1
        array = np.arange(inicio,fin,2)
    return array

array = pares(2,40)

print(array)