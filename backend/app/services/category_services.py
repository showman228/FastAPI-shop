from sqlalchemy.orm import Session
from backend.app.schemas.category import CategoryResponse, CategoryCreate
from backend.app.repositories.category_repositories import CategoryRepository
from fastapi import HTTPException, status
from typing import List

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponse]:
        categories = self.repository.get_all()
        return [CategoryResponse.model_validate(cat) for cat in categories]

    def get_by_id(self, category_id: int) -> CategoryResponse:
        category = self.repository.get_by_id(category_id)
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found",
            )
        return CategoryResponse.model_validate(category)

    def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
        category = self.repository.create(category_data)
        return CategoryResponse.model_validate(category)