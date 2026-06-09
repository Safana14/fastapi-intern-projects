# Day 7 - FastAPI Items API

# Topics Covered
- Path Parameters
- Query Parameters
- Pydantic BaseModel
- Request Body Validation
- POST Endpoint
- HTTPException
- 404 Error Handling
- Endpoints
Get Item by ID

GET /items/{item_id}

Response:

{
"name": "Laptop",
"price": 50000,
"description": "Gaming laptop"
}

Get All Items

GET /items

Response:

[
{
"name": "Laptop",
"price": 50000,
"description": "Gaming laptop"
},
{
"name": "Mouse",
"price": 500,
"description": "Wireless mouse"
}
]

Create Item

POST /items

Response:

{
"message": "Item created successfully",
"item_id": 3
}

Item Not Found

GET /items/100

Response:

{
"detail": "Item not found"
}