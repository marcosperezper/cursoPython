# Mapas de calor (heatmap)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

#Crear mapa de calor en funcion de una matriz
vuelos = sns.load_dataset('flights')
vuelos = vuelos.pivot('month','year','passengers')
# sns.heatmap(vuelos)
# sns.heatmap(vuelos,annot=True,fmt='d')

#Mapa de calor centrado en el valor central
center = vuelos.loc['May'][1956]
# sns.heatmap(vuelos,center=center,annot=True,fmt='d')
sns.heatmap(vuelos,center=center,annot=True,fmt='d',cbar_kws={'orientation':'horizontal'})


plt.pyplot.show()