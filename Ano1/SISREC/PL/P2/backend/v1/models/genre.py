from sqlmodel import Field, SQLModel, JSON
from typing import Optional, List
from sqlalchemy import Column, String


class Genre(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class GenreRead(SQLModel):
    genres: List[str]

class GenreCreate(SQLModel):
    name: str

class GenreReturn(SQLModel):
    name: str

