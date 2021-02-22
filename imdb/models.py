from sqlalchemy import (MetaData, Table, Column,
                        Integer, Float, String,
                        Boolean)
from sqlalchemy.dialects.postgresql import ARRAY


meta = MetaData()

IMDB = Table(
    'imdb',
    meta,
    Column('id', Integer, primary_key=True),
    Column('popularity', Float),
    Column('director', String(length=100)),
    Column('genre', ARRAY(String(length=100))),
    Column('imdb_score', Float),
    Column('name', String(length=200)),
)

User = Table(
    'user',
    meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(length=64), unique=True),
    Column('password', String(length=128)),
    Column('is_admin', Boolean, default=False),
)

