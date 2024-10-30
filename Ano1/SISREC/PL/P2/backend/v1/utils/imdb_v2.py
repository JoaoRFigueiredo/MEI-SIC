import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from dotenv import load_dotenv
import re
from time import sleep
import numpy as np
import pandas as pd

load_dotenv()

url_base = 'https://www.imdb.com/find/?q='

script_dir = os.path.dirname(__file__)

# Read the CSV file into a DataFrame
df_movies = pd.read_csv(os.path.join(script_dir, 'movies.csv'))

# Remove specific elements from every row in the column called "title"
#df_movies['title'] = df_movies['title'].str.replace(r'\(.*?\)', '', regex=True)
df_movies['title'] = df_movies['title'].str.replace(r'\((?![\d]+)\b[^)]+\)', '', regex=True)
df_movies['title'] = df_movies['title'].str.replace('&','')
df_movies['title'] = df_movies['title'].str.replace('(8½)','')
count = 0

def remove_and_extract(string):
    match = re.search(r'\((.*?)\)', string)
    if match:
        extracted = match.group(1)
        modified_string = string.replace(match.group(0), "")
        return modified_string.strip(), extracted.strip()
    else:
        return string.strip(), None

for ind in df_movies.index[0:]:
    url = url_base + df_movies['title'][ind]
    encoded_url = quote(url)
    title = df_movies['title'][ind]
    titleAlt = title.replace('"', '')
    df_movies.at[ind,'title'] = titleAlt
    df_movies.to_csv("./backend/v1/utils/movies_with_imdb.csv", index=False)

    if df_movies.at[ind,'year'] == 0:
        print("Hit")
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find('a', class_='ipc-metadata-list-summary-item__t')['href']
            print(results)
            imdb_id_match = re.search(r'tt(\d+)', results)
            print(imdb_id_match)
            imdb_id = "tt" + imdb_id_match.group(1)
            print(imdb_id)
            modified_string, extracted_value = remove_and_extract(title)
            print("Modified string:", modified_string)  # Output: "Exemplo"
            print("Extracted value:", extracted_value)  # Output: "2024"
            print(imdb_id)
            df_movies.at[ind,'title'] = modified_string
            df_movies.at[ind,'year'] = extracted_value
            df_movies.at[ind,'imdb'] = imdb_id
            df_movies.to_csv("./backend/v1/utils/movies_with_imdb.csv", index=False)
            count += 1
        except Exception as e: 
            print(e)
            pass
    else:
        pass
print(count)

