import pandas as pd
import os
import re
from dotenv import load_dotenv
import requests
from time import sleep




script_dir = os.path.dirname(__file__)



file_path = os.path.join(script_dir,'./movies_with_imdb.csv')

file_path1 = os.path.join(script_dir,'./movies_full.csv')

merged_df = pd.read_csv(file_path1)

merged_df = merged_df.fillna('')
merged_df.to_csv(file_path1, index=False)

#for ind in merged_df.index:
#    merged_df.at[ind,'titleLower'] = merged_df.at[ind,'title'].lower()
#    merged_df.to_csv(file_path1, index=False)
