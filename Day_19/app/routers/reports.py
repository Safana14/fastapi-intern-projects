from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Entry

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/summary")
async def summary_report(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Entry))
    entries = result.scalars().all()

    positive = sum(1 for e in entries if e.sentiment == "POSITIVE")
    negative = sum(1 for e in entries if e.sentiment == "NEGATIVE")

    return {
        "positive": positive,
        "negative": negative,
        "total": len(entries)
    }