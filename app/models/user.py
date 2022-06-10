from pydantic import BaseModel


class User(BaseModel):
    name: str
    description: str | None = None
    phone: int
    email: str | None = None
