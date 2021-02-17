# Crear una array con 100 numeros enteros aleatorios entre el 0 y 500
# Utilizar un diagrama de caja para mostrar los valors aleatorios generados


import numpy as np
import seaborn as sns
import matplotlib as plt



array = np.random.randint(0,500,size=100)

sns.boxplot(array)


plt.pyplot.show()