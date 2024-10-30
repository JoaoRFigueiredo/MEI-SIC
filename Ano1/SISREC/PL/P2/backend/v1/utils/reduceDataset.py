import pandas as pd
import os

script_dir = os.path.dirname(__file__)
tags_df = pd.read_csv(os.path.join(script_dir, "./tags.csv"))
tags_df_novo = os.path.join(script_dir, "./tags_novo.csv")
movies_df = pd.read_csv(os.path.join(script_dir, "./movies_full.csv"))
movies_df_novo = os.path.join(script_dir, "./movies_full_novo.csv")

tags_df.drop(['timestamp', 'userId'], axis=1, inplace=True)
movies_df.drop(['genres','imdbId','year','url','titleLower'], axis=1, inplace=True)

tags_df.to_csv(tags_df_novo, index=False)
movies_df.to_csv(movies_df_novo, index=False)