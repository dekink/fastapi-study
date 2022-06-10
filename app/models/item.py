from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str
    name: str = Field(example='image name')


class Item(BaseModel):
    name: str
    description: str | None = Field(
        defualt=None, title='The description of the item', max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: list[str] = []
    types: set[int] = set()
    image: Image | None = None
    images: list[Image] | None = None

    # class Config:
    #     schema_extra = { # 요청 예시 데이터 여기 필드 다써줘야함
    #         'example': {
    #             'name': 'KDE',
    #             'description': 'iii',
    #             'price': 25.3,
    #             'tax': 2.3
    #         }
    #     }
