from fastapi import FastAPI
from app.routes import tasks, auth
from app.sentiment import get_sentiment_pipeline

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    get_sentiment_pipeline()


app.include_router(auth.router)
app.include_router(tasks.router)