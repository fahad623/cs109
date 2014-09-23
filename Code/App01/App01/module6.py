import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

critics = pd.read_csv(r'C:\Fahad\code\Python-projects\cs109\content-original\critics.csv')


#for this assignment, let's drop rows with missing data
critics = critics[~critics.quote.isnull()]
critics = critics[critics.fresh != 'none']
critics = critics[critics.quote.str.len() > 0]

print critics.shape

text = critics['quote'].values
print text.shape

vectorizer = CountVectorizer(min_df=0)
vectorizer.fit(text)
X = vectorizer.transform(text)
Y = [1 if y == 'fresh' else 0 for y in critics['fresh'].values ]
print Y