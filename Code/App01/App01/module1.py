import numpy as np
import pandas as pd

from collections import defaultdict
import json

predictwise = pd.read_csv('predictwise.csv').set_index('States')
predictwise.head()

print np.random.uniform(0, 1, 3)

mask =  predictwise.Obama > np.random.uniform(0, 1, 51)

dfObama = predictwise[mask]

print dfObama.Votes.sum()


a = np.array([ 3, 5, 7, 8, 9])

print (a > 7).sum()