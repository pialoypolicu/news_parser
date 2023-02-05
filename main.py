import multiprocessing as mp
from typing import List

from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from core_parser import runner_parser
from sql_app.crud import select_query
from sql_app.database import engine, get_session
from sql_app.models import NewsTopic, init_database
from sql_app.schemas import IResponseBase, PostBase
from utils import get_unixtime

app = FastAPI()


@app.on_event('startup')
async def startup():
    await init_database()
    p = mp.Process(target=runner_parser, daemon=True)
    p.start()


@app.on_event('shutdown')
async def shutdown_event():
    await engine.dispose()


@app.get('/metro/news/', response_model=IResponseBase[List[PostBase]], status_code=status.HTTP_200_OK)
async def get_news(response: Response, limit_day: int = 5, db_asession: AsyncSession = Depends(get_session)):
    ts_limit = get_unixtime(limit_day)
    result = await select_query(NewsTopic, ts_limit, db_asession)
    if not result:
        response.status_code = status.HTTP_204_NO_CONTENT
    return {'result': result}
