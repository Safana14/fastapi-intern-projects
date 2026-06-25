from fastapi import FastAPI

from app.routers import entries
from app.routers import reports
from app.routers import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(entries.router)
app.include_router(reports.router)