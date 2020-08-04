# Crear una lista de 1000 valores aleatorio que sigan una distribucion normal
# Crear un histograma mediante matplotlib con la lista de valores
# Crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt


lista_valores = np.random.randn(1000)
# plt.pyplot.hist(lista_valores)

sns.boxplot(lista_valores)





plt.pyplot.show()