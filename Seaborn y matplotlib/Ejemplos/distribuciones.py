#Distribuciones y combinacion de estilos

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

datos = np.random.rand(100)

# sns.distplot(datos, color="green")

#Curva sin el grafico de barras
# sns.distplot(datos,color="green",rug=False,hist=False)

#Cruva e histograma con etiquetas pasando un diccionario como información
# argumentos_curva = {'color':'black','label':'curva'}
# argumentos_histograma = {'color':'grey','label':'histograma'}
# sns.distplot(datos,bins=25,kde_kws=argumentos_curva,hist_kws=argumentos_histograma)

#Cruva e histograma con etiquetas pasando una serie de datos
serie = pd.Series(datos)
sns.distplot(serie,bins=25,color="green")

#Mostrar
plt.pyplot.show()