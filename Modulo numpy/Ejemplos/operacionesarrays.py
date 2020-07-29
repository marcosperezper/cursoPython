#Operaciones con array

import numpy as np

array1 = np.array([1,2,3,4])

# print(array1)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)

array_doble = array_doble * 2
print(array_doble)