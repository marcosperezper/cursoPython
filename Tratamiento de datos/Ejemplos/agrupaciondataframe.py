#Agrupacion de Dataframes   
import numpy as np
import pandas as pd

lista_valores = {'clave1':['x','x','y','y','z'],'clave2':['a','b','a','b','a'],
                'datos1':np.random.rand(5),'datos2':np.random.rand(5)} 

dataframe = pd.DataFrame(lista_valores)


grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])

media = grupo1.mean()

print(media)