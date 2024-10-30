from fastapi import APIRouter, Depends, HTTPException, Query
from models import *
from database import *
from typing import List
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
import csv
import os

router = APIRouter(prefix='/genres', tags=['Genres'])

@router.post("/", response_model=GenreRead, summary="Put genres in the database")
async def getGenres(*, session: AsyncSession = Depends(get_db)):
    lista = []
    script_dir = os.path.dirname(__file__)
    path = r"../recommender/dataset/small_dataset/movies.csv"
    file_path = os.path.join(script_dir, path)
    genre = await session.execute(select(Genre))
    if genre.scalars().all():
        raise HTTPException(status_code=404, detail="The genres were already loaded")
    with open(file_path, "r", encoding="utf8") as file:
            csv_reader = csv.reader(file)
            for linhas in csv_reader:
                genres = linhas[2]
                genresSplit = genres.split("|")
                for genre in genresSplit:
                    if genre in lista:
                        pass
                    else:
                        lista.append(genre)
    lista.remove("genres")
    for item in lista:
        gender = Genre(name=item)
        session.add(gender)
        await session.commit()
    return {"genres": lista}

@router.get("/", response_model=GenreRead, summary="Get all genres")
async def getGenres(*, session: AsyncSession = Depends(get_db)):
    listaGenres = []
    query = select(Genre)
    genres = await session.execute(query)
    allGenres = genres.scalars().all()
    for genre in allGenres:
        listaGenres.append(genre.name)
    return {"genres": listaGenres}

@router.post("/", response_model=GenreReturn, summary="Create a genre")
async def createGenre(*, session: AsyncSession = Depends(get_db), genreCreate: GenreCreate):
    query = select(Genre).where(Genre.name == genreCreate.email)
    genre = await session.execute(query)
    if genre.scalars().first():
        raise HTTPException(status_code=400, detail="Genre already exists")
    db_genre = GenreRead(name=genreCreate.name)
    session.add(db_genre)
    await session.commit()
    await session.refresh(db_genre)
    return db_genre