from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.database import get_db
from app.models import Entry
from app.schemas import EntryCreate, EntryUpdate
from app.sentiment import analyze_sentiment

from app.dependencies import get_current_user
from app.models import User

router = APIRouter(
    prefix="/entries",
    tags=["Entries"]
)


@router.post("/")
async def create_entry(
    data: EntryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = analyze_sentiment(data.text)

    entry = Entry(
    user_id=current_user.id,
    text=data.text,
        sentiment=result["sentiment"],
        score=result["score"]
    )

    db.add(entry)
    await db.commit()
    await db.refresh(entry)

    return {
        "message": "Entry created",
        "sentiment": result["sentiment"],
        "score": result["score"]
    }


@router.get("/")
async def get_entries(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Entry)
        .offset(skip)
        .limit(limit)
    )

    entries = result.scalars().all()

    return entries

@router.get("/{entry_id}")
async def get_entry(
    entry_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Entry).where(
            Entry.id == entry_id
        )
    )

    entry = result.scalar_one_or_none()

    if not entry:
        raise HTTPException(
            status_code=404,
            detail="Entry not found"
        )

    return entry


@router.put("/{entry_id}")
async def update_entry(
    entry_id: int,
    data: EntryUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Entry).where(
            Entry.id == entry_id
        )
    )

    entry = result.scalar_one_or_none()

    if not entry:
        raise HTTPException(
            status_code=404,
            detail="Entry not found"
        )

    result = analyze_sentiment(data.text)

    entry.text = data.text
    entry.sentiment = result["sentiment"]
    entry.score = result["score"]

    await db.commit()
    await db.refresh(entry)

    return entry

@router.delete("/{entry_id}")
async def delete_entry(
    entry_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Entry).where(
            Entry.id == entry_id
        )
    )

    entry = result.scalar_one_or_none()

    if not entry:
        raise HTTPException(
            status_code=404,
            detail="Entry not found"
        )

    await db.delete(entry)
    await db.commit()

    return {
        "message": "Entry deleted successfully"
    }