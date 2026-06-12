from fastapi import FastAPI
from routes.books import router

app = FastAPI()

app.include_router(router)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Books API"}