from sqlmodel import Field, SQLModel, JSON
from typing import Optional, List
from sqlalchemy import Column, String


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    genresLike: Optional[List[str]] = Field(sa_column=Column(JSON))
    genresDislike: Optional[List[str]] = Field(sa_column=Column(JSON))

class UserCreate(SQLModel):
    name: str
    email: str
    password: str


class UserUpdate(SQLModel):
    name: Optional[str]   
    email: Optional[str]   
    password: Optional[str]

class UserLogin(SQLModel): 
    email: str 
    password: str

class UserRead(SQLModel):
    id: int
    name: str 
    email: str  
    password: str
    genresLike: List[str]
    genresDislike: List[str]