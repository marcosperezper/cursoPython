#Reemplazar datos en series 

import numpy as np
import pandas as pd

serie1 =pd.Series([1,2,3,4,5], index=list('abcde'))

serie2 = serie1.replace(1,6)

serie3 = serie1.replace({2:8,3:9})

print(serie3)