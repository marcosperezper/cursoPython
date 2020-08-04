#Regresiones

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

propinas = sns.load_dataset('tips')
# Grafico lineal simple
# sns.lmplot('total_bill','tip',propinas)

#Grafico con marcadores 
# sns.lmplot('total_bill','tip',propinas,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'blue'})

#Grafico sin linea reguladora
# sns.lmplot('total_bill','tip',propinas,fit_reg=False)

#Porcentajes de las propinas
propinas['porcentaje'] = 100 * propinas['tip'] / propinas['total_bill']
# sns.lmplot('size','porcentaje',propinas)

#Comparar las propinas en funcion del sexo
sns.lmplot('total_bill','porcentaje',propinas,hue='sex',markers=['x','o'])

plt.pyplot.show()