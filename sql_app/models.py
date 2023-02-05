from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from sql_app.database import engine


async def init_database():
    async with engine.begin() as connection:
        # await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


class Base(DeclarativeBase):
    pass


class NewsTopic(Base):
    __tablename__ = 'news_topics'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    uri_picture = Column(String)
    uri_post = Column(String, unique=True, nullable=False)
    posted = Column(Integer, nullable=False)
    parsed = Column(Integer, nullable=False)
