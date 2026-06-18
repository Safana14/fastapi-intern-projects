from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Task


async def create_task(db: AsyncSession, task_data):
    task = Task(**task_data.model_dump())

    db.add(task)

    await db.commit()
    await db.refresh(task)

    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(
        select(Task)
    )

    return result.scalars().all()


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )

    return result.scalar_one_or_none()


async def update_task(
    db: AsyncSession,
    task_id: int,
    task_data
):
    task = await get_task(
        db,
        task_id
    )

    if not task:
        return None

    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed

    await db.commit()
    await db.refresh(task)

    return task


async def delete_task(
    db: AsyncSession,
    task_id: int
):
    task = await get_task(
        db,
        task_id
    )

    if not task:
        return None

    await db.delete(task)
    await db.commit()

    return {
        "message": "Task deleted"
    }


async def get_user_tasks(
    db: AsyncSession,
    user_id: int
):
    result = await db.execute(
        select(Task).where(
            Task.user_id == user_id
        )
    )

    return result.scalars().all()