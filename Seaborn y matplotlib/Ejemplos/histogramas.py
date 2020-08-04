#Histogramas

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl

datos1 = np.random.rand(100)
datos2 = np.random.rand(80)
datos3 = np.random.rand(1000)
datos4 = np.random.rand(1000)

# histograma = mpl.pyplot.hist(datos1,color='yellow')
# sns.distplot(datos1,color='green')


# mpl.pyplot.hist(datos2,color='yellow',alpha=0.4)

# mpl.pyplot.hist(datos1,color='green',alpha=0.3,bins=20,density=True)
# mpl.pyplot.hist(datos2,color='blue',alpha=0.5,bins=20,density=True)

sns.jointplot(datos3,datos4,kind="hex")
mpl.pyplot.show()