from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from variables import PGHOST, PGNAME, PGPASS, PGUSER

DATABASE_URL = f'postgresql+asyncpg://{PGUSER}:{PGPASS}@{PGHOST}/{PGNAME}'
# engine = create_async_engine(DATABASE_URL, echo=True)
engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
