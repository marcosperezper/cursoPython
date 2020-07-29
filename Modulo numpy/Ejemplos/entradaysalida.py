#Entrada y salida con arrays

import numpy as np

array = np.arange(6)

np.save('Modulo numpy/Ejemplos/array1s',array)

array1s = np.load('Modulo numpy/Ejemplos/array1s.npy')

array2 = np.arange(8)

np.savez('Modulo numpy/Ejemplos/arrays',x=array,y=array2)

arrays = np.load('Modulo numpy/Ejemplos/arrays.npz')

np.savetxt('Modulo numpy/Ejemplos/mificheroarray.txt',array2,delimiter=',')

array_texto = np.loadtxt('Modulo numpy/Ejemplos/mificheroarray.txt',delimiter=',')

print(array_texto)
