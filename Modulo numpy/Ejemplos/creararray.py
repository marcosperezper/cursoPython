#Crear un array

import numpy as np

prueba = np.arange(1,5,2)


lista1 = [1,2,3,4]
lista2 = [5,6,7,8] 


array1 = np.array(lista1)

lista_doble = (lista1,lista2)
# print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble)