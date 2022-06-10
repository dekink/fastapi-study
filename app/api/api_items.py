from fastapi import APIRouter, Query, Path, Cookie, Header
from pydantic import Required
from app import models

router = APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    item = {
        'name': 'name',
        'price': 3.3,
        'tax': 10.2
    }
    return {"item_id": item_id, "q": q, 'item': item}


@router.get("/items/")
async def read_items(
        # 언더스코터 헤더 허용 안할수도..
        user_agent: str | None = Header(default=None, convert_underscores=False), # 헤더 선언 header사용해야함 안하면 쿼리로 인식
        x_token: list[str] | None = Header(default=None),# 중복헤더
        q: str | None = Query(default=None, min_length=3, max_length=50, regex='^fixedquery$'),
        ads_id: str | None = Cookie(default=None),
):
    results = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
        'ads_id': ads_id,
        'User-Agent': user_agent,
        'X-token': x_token
    }
    if q:
        results.update({"q": q})
    return results


@router.get("/items/required/")
async def read_items_required(
        # requried :  default=... or 안쓰거나
        q: str = Query(default=Required, min_length=3, max_length=50, regex='^fixedquery$')
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}], 'required': True}
    if q:
        results.update({"q": q})
    return results


@router.get('/items/list/')
async def read_items_list(
        q: list[str] | None = Query(
            default=['foo', 'bar'],
            description='리스트 파라미터 입니다.',
            alias='item-query', # 이렇게 바꿔줄수 있다
            include_in_schema=False # docs에서 안보여줌
        )
):
    results = {'item_type': 'list[str]', 'required': False}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/{item_id}/path/')
async def read_items_path(
        *, item_id: int = Path(title="The ID of the item to get"), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


# day 2
# body랑 쿼리랑 섞어서 쓸수있는데 Query 를 명시적으로 쓰는게 더 보기 좋을듯
# pydantic 의존성.. open api스펙과 출동나는 부분 좀 헷갈린다..!
# 동작이 달라지는 부분이 있다
# examples 멋있다... 문서화 희망편...
# swagger 에러가 많다...
# in, Out? or 자기만의 규칙 (req_*, res_*) 별도로 만들어서 관리하는게
# test 코드를 짜야겠다
# pants 세팅 이야기
