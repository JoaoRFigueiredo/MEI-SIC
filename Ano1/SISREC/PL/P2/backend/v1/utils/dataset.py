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

def remove_and_extract(string):
    parts = string.split('(')  # Split the string based on '('
    if len(parts) > 1:  # If there is at least one '('
        extracted = parts[-1].split(')')[0]  # Get the content of the last '('
        modified_string = string.replace(f"({extracted})", "").strip()
        return modified_string, extracted.strip()
    else:
        return string.strip(), None


for ind in merged_df.index[17389:]:
    modified_string, extracted_value = remove_and_extract(merged_df.at[ind,'title'])

    merged_df.at[ind,'title'] = modified_string
    merged_df.at[ind,'year'] = extracted_value

    url = f"https://moviesdatabase.p.rapidapi.com/titles/{merged_df.at[ind,'imdbId']}"

    headers = {
	    "X-RapidAPI-Key": "x",
	    "X-RapidAPI-Host": "x"
    }

    response = requests.get(url, headers=headers)
    json = response.json()
    if json['results'] == None:
        merged_df.at[ind,'url'] = None
        merged_df.to_csv(file_path, index=False)
    elif json['results']['primaryImage'] == None: 
        merged_df.at[ind,'url'] = None
        merged_df.to_csv(file_path, index=False)
    else:
        merged_df.at[ind,'url'] = json['results']['primaryImage']['url']
        merged_df.to_csv(file_path, index=False)
    sleep(3.7)
