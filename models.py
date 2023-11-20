 from pydantic import BaseModel


class Author(BaseModel):
    full_name: str


class Book(BaseModel):
    title: str
    author_id: int


class Client(BaseModel):
    full_name: str
