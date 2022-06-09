from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    name: str
    description: str | None = None
    phone: int
    email: str | None = None


@router.get('/me')
async def read_user_me(user: User):
    return {'user_me': user}
