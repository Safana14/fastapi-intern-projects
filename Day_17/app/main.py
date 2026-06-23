from fastapi import FastAPI
from app.routers import entries, reports

app = FastAPI(title="Sentiment Dashboard API")

app.include_router(entries.router)
app.include_router(reports.router)