from typing import Annotated, Optional
from pydantic import BaseModel
from fastapi import Form


class Todo(BaseModel):
    id: Annotated[Optional[int], "Optional Int"]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!!!!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }


class TodoItems(BaseModel):
    todos: list[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema1!"
                    },
                    {
                        "item": "Example schema2!"
                    }
                ]
            }
        }
