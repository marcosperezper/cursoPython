#Indexacion de arrays

import numpy as np

array = np.arange(0,11)

array_copia = array.copy()

array_copia[0:3] = 20
# print(array_copia)

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2[0,2])