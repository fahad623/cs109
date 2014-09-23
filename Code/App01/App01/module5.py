import pandas as pd
import numpy as np

critics = pd.read_csv(r'C:\Fahad\code\Python-projects\cs109\content-original\critics.csv')


#for this assignment, let's drop rows with missing data
critics = critics[~critics.quote.isnull()]
critics = critics[critics.fresh != 'none']
critics = critics[critics.quote.str.len() > 0]

critics = critics[['critic', 'fresh']]
print critics.shape

critics1 = critics[critics['fresh'] == 'fresh']
print critics1.shape

counts = critics.groupby('critic')
counts1 = critics1.groupby('critic')


print counts.critic.count() > 100

#print counts.fresh.count().head()
#print counts1.fresh.count().head()

#for critic, coundDF in counts1:
#    print critic
#    print coundDF.head()