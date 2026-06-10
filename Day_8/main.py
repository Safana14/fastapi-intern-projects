from fastapi import FastAPI

from models import Product, ProductResponse

app = FastAPI()

products = []

from fastapi import status

@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: Product):
    products.append(product)
    return product

@app.get(
    "/products",
    response_model=list[ProductResponse]
)
def get_products():
    return products


from fastapi import HTTPException

@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):

    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Invalid input data",
            "errors": exc.errors()
        }
    )