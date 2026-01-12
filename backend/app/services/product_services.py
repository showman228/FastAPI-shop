from sqlalchemy.orm import Session
from ..schemas.product import ProductResponse, ProductCreate, ProductListResponse
from ..repositories.product_repositories import ProductRepositories
from ..schemas.category import CategoryResponse, CategoryCreate
from ..repositories.category_repositories import CategoryRepository
from fastapi import HTTPException, status
from typing import List

class ProductServices:
    def __init__(self, db: Session):
        self.repositories_product = ProductRepositories(db)
        self.repositories_category = CategoryRepository(db)

    def get_all_products(self) -> ProductListResponse:
        products = self.repositories_product.get_all()
        products_response = [ProductResponse.model_validate(prod for prod in products)]
        return ProductListResponse(items=products_response, total=len(products_response))

    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.repositories_product.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product by {product_id} not found"
            )
        return ProductResponse.model_validate(product)

    def get_product_by_category(self, category_id: int) -> ProductListResponse:
        category = self.repositories_category.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category by {category_id} not found"
            )
        product = self.repositories_product.get_by_category_id(
            category_id=category_id
        )
        product_response = [ProductResponse.model_validate(prod for prod in product)]
        return ProductListResponse(items=product_response, total=len(product_response))

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.repositories_category.get_by_id(product_data.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category by {product_data.category_id} not found"
            )
        product = self.repositories_product.create(product_data)
        return ProductResponse.model_validate(product)