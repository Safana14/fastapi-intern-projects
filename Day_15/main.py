from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import engine, Base, get_db
from app import models, schema, crud
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Day 14 API"}


# ======================
# AUTH ROUTES
# ======================

@app.post("/auth/register")
async def register(
    user: schema.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(models.User).where(
            models.User.email == user.email
        )
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


@app.post("/auth/login")
async def login(
    user: schema.UserLogin,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(models.User).where(
            models.User.email == user.email
        )
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ======================
# TASK ROUTES
# ======================

@app.post("/tasks")
async def create_task(
    task: schema.TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(
        get_current_user
    )
):
    task_dict = task.model_dump()
    task_dict["user_id"] = current_user.id

    task_obj = models.Task(**task_dict)

    db.add(task_obj)

    await db.commit()
    await db.refresh(task_obj)

    return task_obj


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
    task = await crud.get_task(
        db,
        task_id
    )

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
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(
        get_current_user
    )
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
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(
        get_current_user
    )
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


@app.get("/test123")
async def test123():
    return {"message": "working"}


@app.get("/myday14")
async def myday14():
    return {"message": "THIS IS DAY 14"}