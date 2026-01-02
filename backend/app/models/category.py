from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from backend.app.database import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    slug = Column(String, unique=True, index=True)

    products = relationship("Product", back_populates="category") # связь с категориями с товарами

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"