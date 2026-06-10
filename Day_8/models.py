from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    id: int
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Product Name"
    )
    price: float = Field(
        gt=0,
        description="Price must be greater than zero"
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Product name cannot be empty")
        return value.title()


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float