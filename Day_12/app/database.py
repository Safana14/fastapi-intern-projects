from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "postgresql+asyncpg://postgres:root@localhost/intern_db"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()