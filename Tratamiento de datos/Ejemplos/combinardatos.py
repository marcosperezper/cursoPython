#Combinacion de series y dataframes 

import pandas as pd
import numpy as np


serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6])

serie3 = serie1.combine_first(serie2)
# print(serie3)

lista_valores = [1,2,np.nan]
lista_valores2 = [4,5,6]
dataframe1 = pd.DataFrame(lista_valores)
dataframe2 = pd.DataFrame(lista_valores2)

dataframe3 = dataframe1.combine_first(dataframe2)
print(dataframe3)