from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
from sqlmodel import SQLModel
load_dotenv()

engine = create_async_engine(os.getenv('DATABASE_URL_TEST'),  echo=True, future=True)
SessionLocal = async_sessionmaker(engine)

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
