# News parser

##### Описание.

Данный проект включает в себя парсер новостей и возможность запроса новостных постов из БД.

#### api anepoint
_/metro/news/_

params: limit_day: int

ex: http://127.0.0.1/metro/news/?limit_day=5

#### Стек/зависимости
```
Python3.10
AsyncIO
fastapi
pytest
aiohttp
beautifulsoup4
```

##### Запуск проекта из командной строки
1. склонировать репозиторий выполнив команду
> `git clone https://github.com/pialoypolicu/news_parser.git`
2. установить вирт окружение 
> `python3 -m venv venv`
3. активируем виртуальное окружение
> `source venv/bin/activate` 
4. обновляем pip пакет
> `pip install --upgrade pip`
5. устанавливаем зависимости
> `pip install -r requirements.txt`
6. Создать БД PostgreSQL.
7. создать файл .env и внести в него конфиденциальную информацию, в соответствии с вашей БД.
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`DB_HOST`
`POSTGRES_DB`
8. запустить скрипт возможно командой 
> `uvicorn main:app --host 0.0.0.0 --reload`


##### Запуск проекта в docker
1. склонировать репозиторий выполнив команду
> `git clone https://github.com/pialoypolicu/news_parser.git`
2. создать файл .env  и внести в него конфиденциальную информацию, в соответствии с вашей БД.
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`DB_HOST`
`POSTGRES_DB`
3. запустить docker в командной строке, находясь в корневой директории проекта 
> `docker-compose up`


#### tests
Для запуска тестов выполните команду 
> `pytest -vv`
