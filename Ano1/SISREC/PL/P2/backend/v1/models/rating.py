from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from .movie import Movie



class Rating(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    movie_id: int | None = Field(default=None, foreign_key="movie.movieid")
    stars: float
    timestamp: int

class RatingCreate(SQLModel):
    user_id: int
    movie_id: int
    stars: float

class RatingReturn(SQLModel):
    id: Optional[int]
    user_id: int
    movie_id: int
    stars: float
    timestamp: int
    titleMovie: str | None = None
    genresMovie: str | None = None
    imdbidMovie: str | None = None
    yearMovie: int | None = None
    urlMovie: str | None = None


def rating_to_rating_return(rating: Rating) -> RatingReturn:
    return RatingReturn(
        id=rating.id,
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        stars=rating.stars,
        timestamp=rating.timestamp
    )

def list_rating_to_list_rating_return(ratings: List[Rating]) -> List[RatingReturn]:
    return [rating_to_rating_return(rating) for rating in ratings]
