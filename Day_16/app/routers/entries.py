from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Entry
from app.schemas import EntryCreate
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