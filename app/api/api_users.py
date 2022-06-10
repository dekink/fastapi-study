from fastapi import APIRouter
from app import models

router = APIRouter()


@router.get('/me')
async def read_user_me(user: models.user.User):
    return {'user_me': user}
