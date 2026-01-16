from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Category name") # 3 точки обозначают что поле должно быть обязательно заполнено
    slug: str = Field(..., min_length=5, max_length=100, description="URl - friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int  = Field(..., description="Unique category ID")

    class Config:
        from_attributes = True # позволяет напрямую создавать схему напрямую из модели


