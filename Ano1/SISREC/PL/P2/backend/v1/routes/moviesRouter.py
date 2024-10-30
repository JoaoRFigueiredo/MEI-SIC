from fastapi import APIRouter, Depends, HTTPException, Query
from models import *
from database import *
from typing import List
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from fastapi.responses import JSONResponse
import csv
import os
import pandas as pd
from random import randint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter(prefix='/movies', tags=['Movies'])

@router.get("/search/{title}", summary="Search movie")
async def getMovie(*, session: AsyncSession = Depends(get_db), title: str):
    titleAlt = title.lower()
    query = select(Movie).where(Movie.titlelower.contains(titleAlt)).limit(5)
    movies = await session.execute(query)
    allMovies = movies.scalars().all()
    return allMovies

@router.get("/randomMovie", summary="Returns random movie")
async def getRandomMovie(*, session: AsyncSession = Depends(get_db)):
    number = randint(0, 62423)
    print(f" Number that has selected :{number}")
    movie = await session.get(Movie, number)
    return movie

script_dir = os.path.dirname(__file__)
tags_df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/tags.csv"))
movies_df = pd.read_csv(os.path.join(script_dir, "../utils/small_dataset/movies_full_2.csv"))
tags_df.set_index('movieId', inplace=True)
movies_df.set_index('movieId', inplace=True)
tags_df['tag'] = tags_df['tag'].str.lower()
tags_df['tag'] = tags_df['tag'].astype(str)
movie_tags = tags_df.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
movies = pd.merge(movies_df, movie_tags, on='movieId', how='left')
movies['tag'] = movies['tag'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['tag'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

@router.get("/similarMovies/{title}", summary="Returns 5 similar movies")
async def getSimilarMovies(*, title: str):
    matching_rows = movies[movies['title'].str.contains(title, case=False, na=False)]
    if len(matching_rows) == 0:
        return []
    idx = matching_rows.index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6] 
    
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 5 similar movies
    return movies['title'].iloc[movie_indices].tolist()