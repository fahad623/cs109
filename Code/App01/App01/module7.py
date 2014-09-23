import pandas as pd
import numpy as np

df = pd.DataFrame({'value': np.random.randint(0, 100, 20)})

labels = [ "{0} - {1}".format(i, i + 9) for i in range(0, 100, 10) ]

cuts = pd.cut(df.value, range(0, 105, 10))

bins = np.linspace(0, 1, 20)
print bins
print bins[:-1]
print bins[1:]
import json