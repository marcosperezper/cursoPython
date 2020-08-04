#Diagramas de caja
#Representar una serie de datos númericos a traves den sus cuartiles

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

datos = np.random.randn(100)

sns.boxplot(datos)

plt.pyplot.show()