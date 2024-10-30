from sqlmodel import Field, SQLModel
from typing import Optional


class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movieid: int
    title: str
    titlelower: str
    genres: str
    imdbid: str
    year: int | None = None
    url: str | None = None