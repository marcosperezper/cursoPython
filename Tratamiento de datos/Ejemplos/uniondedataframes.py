# Union de dataframes
import pandas as pd

dataframe1 = pd.DataFrame({'c1' : ['1','2','3'], 'clave' : ['a','b','c']})
dataframe2 = pd.DataFrame({'c2' : ['4','5','6'], 'clave' : ['c','b','e']})

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2)
# dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave')
# dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='left')
# dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='right')
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='outer')
print(dataframe4) 