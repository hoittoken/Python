import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, String, create_engine, text
from config import settings

sync_engine = create_engine(
    url=settings.DATABES_URL_psycopg,
    echo=True,
    pool_size=3,
    max_overflow=2
)

session_factory = sessionmaker(sync_engine)

str_100 = Annotated[str, 100]
str_320 = Annotated[str, 320]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_100: String(100),
        str_320: String(320)
    }

'''
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=3,
    max_overflow=2
)


with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT * FROM cloveri.interns"))
    print(f"{res.all()}")
    


async def a_func():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT * FROM cloveri.interns"))
        print(f"{res.all()}")

asyncio.run(a_func())
'''