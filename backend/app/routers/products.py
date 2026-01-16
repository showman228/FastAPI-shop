from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.product import ProductResponse, ProductListResponse
from ..services.product_services import ProductServices

router = APIRouter (
    prefix="/api/products",
    tags=["products"]
)

@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    services = ProductServices(db)
    return services.get_all_products()

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    services = ProductServices(db)
    return services.get_product_by_id(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_product_by_category(category_id: int, db: Session = Depends(get_db)):
    services = ProductServices(db)
    return services.get_product_by_category(category_id)
