from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncConnection

from app.database import engine, Base
from app import models

app = FastAPI()


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )


@app.get("/")
async def root():
    return {"message": "Day 11 API"}


@app.on_event("startup")
async def startup():
    print("Creating tables...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("Tables created!")


from fastapi import FastAPI

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    }
]


@app.get("/tasks")
async def get_tasks():
    return tasks