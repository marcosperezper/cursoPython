#Concatenacion de arrays,series y dataframes

import pandas as pd
import numpy as np

array1 = np.arange(9).reshape(3,3)

# array_concat = np.concatenate([array1,array1])
array_concat = np.concatenate([array1,array1],axis=1)
# print(array_concat)

serie1 = pd.Series([1,2,3],index=['a','b','c'])
serie2 = pd.Series([4,5,6],index=['d','e','f'])

serie_concat = pd.concat([serie1,serie2],keys=['serie1','serie2'])
# print(serie_concat)

dataframe1 = pd.DataFrame(np.random.rand(3,3),columns=['a','b','c'])
dataframe2 = pd.DataFrame(np.random.rand(2,3),columns=['a','b','c'])
# dataframe_contact = pd.concat([dataframe1,dataframe2])
dataframe_contact = pd.concat([dataframe1,dataframe2],ignore_index=True)
print(dataframe_contact)