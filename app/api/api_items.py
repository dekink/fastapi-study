from fastapi import APIRouter, Query
from pydantic import Required

router = APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@router.get("/items/")
async def read_items(
        q: str | None = Query(default=None, min_length=3, max_length=50, regex='^fixedquery$')
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
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
async def read_items_list(q: list[str] | None = None):
    results = {'item_type': 'list[str]', 'required': False}
    if q:
        results.update({'q': q})
    return results
