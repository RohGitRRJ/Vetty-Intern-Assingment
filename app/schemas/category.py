from pydantic import BaseModel


class Category(BaseModel):
    category_id: str
    name: str


class CategoryListResponse(BaseModel):
    items: list[Category]
