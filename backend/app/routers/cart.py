from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict
from backend.app.database import get_db
from ..schemas.cart import CartResponse, CartItemCreate, CartItemUpdate
from ..services.cart_services import CartService
from pydantic import BaseModel

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}

class UpdateCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}

class RemoveFromCartRequest(BaseModel):
    cart: Dict[int, int] = {}


@router.post("/add", status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    services = CartService(db)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = services.add_to_cart(cart_data=request.cart, item=item)
    return {"cart": updated_cart}

router.get("", response_model=CartResponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int, int], db: Session = Depends(get_db)):
    services = CartService(db)
    return services.get_cart_details(cart_data)
    
@router.put("update", status_code=status.HTTP_200_OK)
def update_cart(request: UpdateCartRequest, db: Session = Depends(get_db)):
    services = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    update_cart = services.update_cart_item(cart_data=request.cart, item=item)
    return {"cart": update_cart}

@router.delete("remove/{product_id}", status_code=status.HTTP_200_OK)
def remove_from_cart(product_id: int, request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    services = CartService(db)
    update_cart = services.remove_from_cart(cart_data=request.cart, product_id=product_id)
    return {"cart": update_cart}