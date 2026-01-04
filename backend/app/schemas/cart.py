from pydantic import BaseModel, Field
from typing import Optional, List

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Unique product ID")
    quantity: int = Field(..., gt=0, description="Quantity of product")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Unique product ID")
    quantity: int = Field(..., gt=0, description="New quantity of product")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Price of product")
    quantity: int = Field(..., gt=0, description="Quantity in cart")
    subtotal: float = Field(..., gt=0, description="Subtotal of this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")

class CartResponse(BaseModel):
    items: List[CartItem] = Field(..., description="List of items in a cart")
    total: float = Field(..., gt=0, description="Total value of items in cart")
    items_count: int = Field(..., description="Total number of items in cart")