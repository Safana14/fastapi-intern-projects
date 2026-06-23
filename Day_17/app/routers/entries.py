from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Entry
from app.schemas import EntryCreate, EntryUpdate
from app.sentiment import analyze_sentiment

router = APIRouter(
    prefix="/entries",
    tags=["Entries"]
)


@router.post("/")
async def create_entry(
    data: EntryCreate,
    db: AsyncSession = Depends(get_db)
):
    result = analyze_sentiment(data.text)

    entry = Entry(
        
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
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Entry))
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
        return {"message": "Entry not found"}

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
        return {"message": "Entry not found"}

    sentiment_result = analyze_sentiment(
        data.text
    )

    entry.text = data.text
    entry.sentiment = sentiment_result["sentiment"]
    entry.score = sentiment_result["score"]

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
        return {"message": "Entry not found"}

    await db.delete(entry)
    await db.commit()

    return {
        "message": "Entry deleted"
    }