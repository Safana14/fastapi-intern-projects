from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import engine, Base, get_db
from app import models, schema, crud

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Day 13 API"}


@app.post("/tasks")
async def create_task(
    task: schema.TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_task(db, task)


@app.get("/tasks")
async def get_tasks(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_tasks(db)


@app.get("/tasks/{task_id}")
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    task = await crud.get_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put("/tasks/{task_id}")
async def update_task(
    task_id: int,
    task: schema.TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.update_task(
        db,
        task_id,
        task
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@app.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    deleted = await crud.delete_task(
        db,
        task_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return deleted


@app.get("/users/{user_id}/tasks")
async def get_user_tasks(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_user_tasks(
        db,
        user_id
    )