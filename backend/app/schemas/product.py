from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from backend.app.schemas.category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=250, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price")
    category_id: int = Field(..., description="category id")
    image_url: Optional[str] = Field(None, description="Product image url")

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description="Unique product id")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")

    class Config:
        form_attributes = True


class ProductListResponse(BaseModel):
    items: List[ProductResponse]
    total: int = Field(..., description="Total product count")
