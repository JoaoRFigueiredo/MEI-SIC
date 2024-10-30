import pandas as pd
import os
import re
from dotenv import load_dotenv
import requests
from time import sleep

load_dotenv()

url_base = 'https://www.imdb.com/find/?q='


script_dir = os.path.dirname(__file__)

#df_movie = pd.read_csv(os.path.join(script_dir,'../recommender/dataset/movies.csv'))
#dtype_dict = {'imdbId': str}
#df_links = pd.read_csv(os.path.join(script_dir,'../recommender/dataset/links.csv'), dtype=dtype_dict)
#merged_df = pd.merge(df_movie, df_links[['movieId','imdbId']], on='movieId', how='inner')
#merged_df['imdbId'] = 'tt' + merged_df['imdbId'].astype(str)

file_path = os.path.join(script_dir,'./movies_with_imdb.csv')

#try:
#    f = open(file_path, "x")
#except:
#    pass
merged_df = pd.read_csv(file_path)


for ind in merged_df[merged_df['year'].isnull()].index.tolist():

    url = f"https://moviesdatabase.p.rapidapi.com/titles/{merged_df.at[ind,'imdbId']}"

    headers = {
	    'X-RapidAPI-Key': '174a58e097msh81d5098306d3361p11bf32jsn1f72518f466c',
        'X-RapidAPI-Host': 'moviesdatabase.p.rapidapi.com'
    }
    print(ind)
    response = requests.get(url, headers=headers)
    json = response.json()
    if json['results']['releaseYear'] == None:
        merged_df.at[ind,'year'] = None
        merged_df.to_csv(file_path, index=False)
    else:
        merged_df.at[ind,'year'] = json['results']['releaseYear']['year']
        merged_df.to_csv(file_path, index=False)
