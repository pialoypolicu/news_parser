import os

from dotenv import load_dotenv

load_dotenv('.env')

ALGORITHM = os.getenv('ALGORITHM')

PGUSER = os.getenv('POSTGRES_USER')
PGPASS = os.getenv('POSTGRES_PASSWORD')
PGHOST = os.getenv('DB_HOST')
PGNAME = os.getenv('POSTGRES_DB')
