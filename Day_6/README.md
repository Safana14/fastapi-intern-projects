# Day 6 - FastAPI Basics

## Topics Covered

- FastAPI Installation
- Uvicorn Server
- GET Endpoint
- Health Check Endpoint
- Swagger UI
- ReDoc Documentation

## Endpoints

### Root Endpoint

GET /

Response:

{
  "message": "Hello World"
}

### Health Endpoint

GET /health

Response:

{
  "status": "ok"
}