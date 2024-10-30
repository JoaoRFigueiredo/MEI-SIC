from fastapi import APIRouter, Depends, HTTPException, Query
from models import *
from database import *
from typing import List
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from sqlalchemy import desc

router = APIRouter(prefix='/users', tags=['Users'])

@router.post("/", response_model=UserRead, summary="Create a user")
async def createUser(*, session: AsyncSession = Depends(get_db), userCreate: UserCreate):
    lastUserIdPlusOne = 0
    query = select(User).where(User.email == userCreate.email)
    user = await session.execute(query)
    if user.scalars().first():
        raise HTTPException(status_code=400, detail="User already exists with this email")
    result = await session.execute(select(User).order_by(desc(User.id)))
    lastUser = result.scalars().first()
    if not lastUser:
        lastUserIdPlusOne = 200000
    else:
        lastUserIdPlusOne = lastUser.id + 1
    db_user = User(id=lastUserIdPlusOne,name=userCreate.name, email=userCreate.email, password=userCreate.password, genresLike=[], genresDislike=[])
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.post("/genres/{email}", summary="Add genres to a user")
async def addGenresToUser(*, session: AsyncSession = Depends(get_db), email: str, genresLike: List[str], genresDislike: List[str]):
    query = select(User).where(User.email == email)
    # Change genres to the user
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.genresLike = genresLike
    user.genresDislike = genresDislike
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@router.post("/login", summary="Login")
async def loginUser(*, session: AsyncSession = Depends(get_db), userLogin: UserLogin):
    query = select(User).where(User.email == userLogin.email).where(User.password == userLogin.password)
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found or login credencials are wrong")
    else:
        return {"status": "Verified", "userId": user.id}

@router.get("/{id}", response_model=UserRead, summary="Get user by id")
async def getUserByID(*, session: AsyncSession = Depends(get_db), id: int):
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.patch("/{id}", response_model=UserRead, summary="Update a user")
async def update_user(*, session: AsyncSession = Depends(get_db), id: int, user: UserUpdate):
    db_user = await session.get(User, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    values = user.dict(exclude_unset=True)
    for k, v in values.items():
        setattr(db_user, k, v)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user
                     



