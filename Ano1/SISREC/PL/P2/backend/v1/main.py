import uvicorn
from database import *
from fastapi import FastAPI
from routes import checkRouter, userRouter,genresRouter, recommendationRouter, moviesRouter, ratingRouter
from models import *
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app:FastAPI):
    scheduler = BackgroundScheduler()
    recommendationRouter.nonPersonalizedToFile()
    scheduler.add_job(recommendationRouter.nonPersonalizedToFile,"interval",hours = 1)
    scheduler.start()
    yield

app = FastAPI(lifespan=lifespan)

origins = [    "*",  # Adicione a origem do seu frontend Angular aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(checkRouter.router)
app.include_router(userRouter.router)
app.include_router(genresRouter.router)
app.include_router(recommendationRouter.router)
app.include_router(moviesRouter.router)
app.include_router(ratingRouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000, log_level="info")