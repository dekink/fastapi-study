from fastapi import APIRouter, Body
from app import models

router = APIRouter()


@router.post("/", response_model=models.user.UserOut)
async def create_user(user: models.user.UserIn):
    return user


@router.get('/me')
async def read_user_me(user: models.user.User):
    return {'user_me': user}


@router.put('/{user_id}/')
async def update_user(
        user_id: int,
        user: models.user.User,
        item: models.item.Item,
        importance: int = Body(example=999) # body로 넣어줄수 있다
):
    return {'user_id': user_id, 'user': user, 'item': item, 'importance': importance}


@router.put('/{user_id}/body_embed')
async def update_user_body_embed(
        user_id: int,
        item: models.item.Item = Body(embed=True)
):
    return {'user_id': user_id, 'item': item}


@router.put('/{user_id}/example')
async def update_user_example(
        user_id: int,
        # user: models.user.User, multiple body에서는 example이 안먹음
        item: models.item.Item = Body(
            example={
                'name': 'ex',
                'description': 'hi',
                'price': 99.99,
                'tax': 3.2
            }
        ),
):
    return {'user_id': user_id, 'item': item}


@router.put('/{user_id}/multiple_example')
async def update_user_multiple_example(
        user_id: int,
        item: models.item.Item = Body(
            examples={  #examples!
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            }
        ),
):
    return {'user_id': user_id, 'item': item}