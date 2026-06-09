from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

items_db = {
    1: {
        "name": "Laptop",
        "price": 50000,
        "description": "Gaming laptop"
    },
    2: {
        "name": "Mouse",
        "price": 500,
        "description": "Wireless mouse"
    }
}

@app.get("/")
def home():
    return {"message": "Items API"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return items_db[item_id]

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    item_list = list(items_db.values())
    return item_list[skip : skip + limit]

@app.post("/items")
def create_item(item: Item):
    new_id = max(items_db.keys()) + 1

    items_db[new_id] = item.model_dump()

    return {
        "message": "Item created successfully",
        "item_id": new_id,
        "item": item
    }