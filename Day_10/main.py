from fastapi import FastAPI
from routes.books import router

app = FastAPI()

app.include_router(router)