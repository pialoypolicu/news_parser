from typing import Any, Sequence

from sqlalchemy import Row, RowMapping, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from sql_app.database import async_session
from sql_app.models import NewsTopic


async def creat_rows(data: list) -> None:
    db = async_session()
    await db.execute(insert(NewsTopic).on_conflict_do_nothing(index_elements=['uri_post']), data)
    await db.commit()


async def select_query(model: DeclarativeAttributeIntercept, value: int, db: AsyncSession) -> Sequence[
    Row | RowMapping | Any]:
    query = select(model).order_by(model.posted.desc()).where(model.posted >= value)
    result = await db.scalars(query)
    return result.all()
