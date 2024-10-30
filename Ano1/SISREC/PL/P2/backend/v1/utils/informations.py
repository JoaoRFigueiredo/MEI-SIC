import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from dotenv import load_dotenv
import re
from time import sleep
import numpy as np

load_dotenv()

url_base = 'https://www.imdb.com/find/?q='

script_dir = os.path.dirname(__file__)

# Read the CSV file into a DataFrame
df_movies = pd.read_csv(os.path.join(script_dir, 'movies.csv'))

# Remove specific elements from every row in the column called "title"
#df_movies['title'] = df_movies['title'].str.replace(r'\(.*?\)', '', regex=True)
df_movies['title'] = df_movies['title'].str.replace(r'\((?![\d]+)\b[^)]+\)', '', regex=True)
df_movies['title'] = df_movies['title'].str.replace('&','')
df_movies['title'] = df_movies['title'].str.replace('"','')
df_movies['title'] = df_movies['title'].str.replace('(8½)','')
if 'year' not in df_movies.columns:
    df_movies['year'] = 0
    df_movies['year'] = df_movies['year'].astype(int)

for ind in df_movies.index[1131:]:
    print(df_movies['title'][ind])
    url = url_base + df_movies['title'][ind] + "&ref_=fn_al"
    encoded_url = quote(url, safe=':/?&=')
    try:
        response = requests.get(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find('a', class_='ipc-metadata-list-summary-item__t')['href']
        imdb_id_match = re.search(r'tt(\d+)', results)
        imdb_id = "tt" + imdb_id_match.group(1)
        print(imdb_id)
        df_movies.at[ind,'imdb'] = imdb_id
    except:
        pass
    
    sleep(3.65)
    url = f"https://moviesdatabase.p.rapidapi.com/titles/{imdb_id}"

    headers = {
	    "X-RapidAPI-Key": "174a58e097msh81d5098306d3361p11bf32jsn1f72518f466c",
	    "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    json = response.json()
    if json['results'] == None:
        url = url_base + df_movies['title'][ind] + "&s=tt&ttype=ft&ref_=fn_ft"
        encoded_url = quote(url, safe=':/?&=')
        try:
            response = requests.get(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find('a', class_='ipc-metadata-list-summary-item__t')['href']
            imdb_id_match = re.search(r'tt(\d+)', results)
            imdb_id = "tt" + imdb_id_match.group(1)
            print(imdb_id)
            df_movies.at[ind,'imdb'] = imdb_id
        except:
            pass
        sleep(3.65)
        url = f"https://moviesdatabase.p.rapidapi.com/titles/{imdb_id}"

        headers = {
	        "X-RapidAPI-Key": "174a58e097msh81d5098306d3361p11bf32jsn1f72518f466c",
	        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        json = response.json()
        if json['results']['primaryImage'] == None: 
            split_title = df_movies['title'][ind].split("(")
            title = split_title[0].strip()
            try:
                year = int(split_title[1].replace(")", "").strip())
                df_movies.at[ind,'title'] = json['results']['titleText']['text']
                df_movies.at[ind,'year'] = int(json['results']['releaseYear']['year'])
                df_movies.at[ind,'image_url'] = None
                df_movies.to_csv("./backend/v1/utils/movies.csv", index=False)
            except:
                df_movies.at[ind,'title'] = json['results']['titleText']['text']
                df_movies.at[ind,'year'] = int(json['results']['releaseYear']['year'])
                df_movies.at[ind,'image_url'] = None
                df_movies.to_csv("./backend/v1/utils/movies.csv", index=False)
                pass
    if json['results']['primaryImage'] == None: 
        split_title = df_movies['title'][ind].split("(")
        title = split_title[0].strip()
        df_movies.at[ind,'title'] = json['results']['titleText']['text']
        if json['results']['releaseYear'] == None:
            year = int(split_title[1].replace(")", "").strip())
            df_movies.at[ind,'year'] = int(year)
            df_movies.at[ind,'image_url'] = None
            df_movies.to_csv("./backend/v1/utils/movies.csv", index=False)
        else:
            df_movies.at[ind,'year'] = int(json['results']['releaseYear']['year'])
            df_movies.at[ind,'image_url'] = None
            df_movies.to_csv("./backend/v1/utils/movies.csv", index=False)
    if json['results']['primaryImage'] != None:
        df_movies.at[ind,'title'] = json['results']['titleText']['text']
        df_movies.at[ind,'year'] = int(json['results']['releaseYear']['year'])
        df_movies.at[ind,'image_url'] = json['results']['primaryImage']['url']
        df_movies.to_csv("./backend/v1/utils/movies.csv", index=False)
