import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#api_key = 'wh7z4wpjqbjm9v7u2xsfcu6f'
#movie_id = '770672122'  # toy story 3
#url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

##these are "get parameters"
#options = {'review_type': 'top_critic', 'page_limit': 20, 'page': 1, 'apikey': api_key}
#data = requests.get(url, params=options).text
#data = json.loads(data)  # load a json string into a collection of lists and dicts

#print json.dumps(data['reviews'][0], indent=2)  # dump an object into a json string

from io import StringIO  
movie_txt = requests.get('https://raw.github.com/cs109/cs109_data/master/movies.dat').text
movie_file = StringIO(movie_txt) # treat a string like a file
movies = pd.read_csv(movie_file, delimiter='\t')

#print the first row
#movies[['id', 'title', 'imdbID', 'year']].irow(0)

def fetch_reviews(movies, row):
    imdbID = movies.irow(row).imdbID
    imdbID = '0000000' + str(imdbID)
    imdbID = imdbID[-7:]
    api_key = 'wh7z4wpjqbjm9v7u2xsfcu6f'
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json'
    options = {'id': imdbID, 'type': 'imdb', 'apikey': api_key}
    data = requests.get(url, params=options).text
    data = json.loads(data)
    movie_id = 0
    movie_id = data['id']
    print movie_id
    if movie_id > 0:
        url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id
        options = {'review_type':'top_critic', 'page_limit':20, 'page':1, 'apikey':api_key}
        data = requests.get(url, params=options).text
        data = json.loads(data)
        frame = pd.DataFrame(data['reviews'])
        frame.drop(['links', 'original_score'],inplace=True,axis=1) 
        frame.rename(columns={'freshness': 'fresh', 'date': 'review_date'}, inplace=True)
        frame['imdb'] = imdbID
        frame['rtid'] = movie_id
        frame['title'] = movies.irow(row).title
        return frame
        #print frame.head()
    else:
        return None

rows = 30

dfs = [fetch_reviews(movies, r) for r in range(rows)]
pd = pd.concat(dfs, ignore_index=True)
print pd.head()
