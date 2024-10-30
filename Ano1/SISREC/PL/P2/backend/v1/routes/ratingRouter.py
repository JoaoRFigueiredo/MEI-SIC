from fastapi import APIRouter, Depends, HTTPException, Query
from models import *
from database import *
from typing import List
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select, text
from sqlalchemy import desc
from time import time
import csv

router = APIRouter(prefix='/ratings', tags=['Ratings'])

@router.post("/", summary="Create a rating")
async def createRating(*, session: AsyncSession = Depends(get_db), ratingCreate: RatingCreate):
    script_dir = os.path.dirname(__file__)
    query = select(Rating).where(Rating.user_id == ratingCreate.user_id).where(Rating.movie_id == ratingCreate.movie_id)
    result = await session.execute(query)
    rating = result.scalars().first()
    if rating:
        raise HTTPException(status_code=404, detail="Rating already exists for this user and movie")
    current_timestamp = time()
    intCurrent = int(current_timestamp)
    db_rating = Rating(user_id=ratingCreate.user_id, movie_id=ratingCreate.movie_id, stars=ratingCreate.stars, timestamp=intCurrent)
    session.add(db_rating)
    await session.commit()
    await session.refresh(db_rating)
    fields=[ratingCreate.user_id,ratingCreate.movie_id,ratingCreate.stars, intCurrent]
    path = os.path.join(script_dir, '../recommender/dataset/small_dataset/ratings.csv')
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    return db_rating

@router.get("/", summary="Get a rating by user and movie")
async def getRating(*, session: AsyncSession = Depends(get_db), user_id: int, movie_id: int):
    query = (
        select(Rating.id, 
               Rating.movie_id, 
               Rating.user_id, 
               Rating.stars, 
               Rating.timestamp, 
               Movie.title, 
               Movie.titlelower, 
               Movie.genres, 
               Movie.imdbid, 
               Movie.year, 
               Movie.url)  
        .join(Movie)  
        .where(Rating.user_id == user_id)
        .where(Rating.movie_id == movie_id)
    )
    result = await session.execute(query)
    ratings_with_info = result.fetchone()
    if not ratings_with_info:
        raise HTTPException(status_code=404, detail="Ratings not found")
    rating_dict = {
        "id": ratings_with_info[0],
        "movieId": ratings_with_info[1],
        "userId": ratings_with_info[2],
        "stars": ratings_with_info[3],
        "timestamp": ratings_with_info[4],
        "title": ratings_with_info[5],
        "titleLower": ratings_with_info[6],
        "genres": ratings_with_info[7],
        "imdbId": ratings_with_info[8],
        "year": ratings_with_info[9],
        "url": ratings_with_info[10]
    }
    
    return rating_dict

@router.get("/history/{userid}", summary="Get last 5 ratings of a user")
async def getRatings(*, session: AsyncSession = Depends(get_db), userid: int):
    query = (
        select(Rating.id, 
               Rating.movie_id, 
               Rating.user_id, 
               Rating.stars, 
               Rating.timestamp, 
               Movie.title, 
               Movie.titlelower, 
               Movie.genres, 
               Movie.imdbid, 
               Movie.year, 
               Movie.url)  
        .join(Movie)
        .where(Rating.user_id == userid)
        .order_by(desc(Rating.timestamp))
        .limit(5)
    )
    result = await session.execute(query)
    ratings_with_info = result.fetchall()
    if not ratings_with_info:
        raise HTTPException(status_code=404, detail="Ratings not found")
    structured_response = []
    for rating_info in ratings_with_info:
        rating_dict = {
            "id": rating_info[0],
            "movieId": rating_info[1],
            "userId": rating_info[2],
            "stars": rating_info[3],
            "timestamp": rating_info[4],
            "title": rating_info[5],
            "titleLower": rating_info[6],
            "genres": rating_info[7],
            "imdbId": rating_info[8],
            "year": rating_info[9],
            "url": rating_info[10]
        }
        structured_response.append(rating_dict)
    
    return structured_response


@router.get("/favoriteMovies/{userid}", summary="Get favorite movies of a user")
async def favoriteMovie(*, session: AsyncSession = Depends(get_db), userid: int):
    query = (
        select(Rating.id, 
               Rating.movie_id, 
               Rating.user_id, 
               Rating.stars, 
               Rating.timestamp, 
               Movie.title, 
               Movie.titlelower, 
               Movie.genres, 
               Movie.imdbid, 
               Movie.year, 
               Movie.url)  
        .join(Movie)
        .where(Rating.user_id == userid)
        .order_by(desc(Rating.stars))
        .order_by(desc(Rating.timestamp))
        .limit(5)
    )
    result = await session.execute(query)
    ratings_with_info = result.fetchall()
    if not ratings_with_info:
        raise HTTPException(status_code=404, detail="Ratings not found")
    structured_response = []
    for rating_info in ratings_with_info:
        rating_dict = {
            "id": rating_info[0],
            "movieId": rating_info[1],
            "userId": rating_info[2],
            "stars": rating_info[3],
            "timestamp": rating_info[4],
            "title": rating_info[5],
            "titleLower": rating_info[6],
            "genres": rating_info[7],
            "imdbId": rating_info[8],
            "year": rating_info[9],
            "url": rating_info[10]
        }
        structured_response.append(rating_dict)
    
    return structured_response
