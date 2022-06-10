from fastapi import Request, APIRouter, Depends
from pydantic import create_model

router = APIRouter()


@router.get("/request/{request_id}")
def read_root(request_id: str, request: Request):
    client_host = request.client.host
    # request 를 직접 사용
    kwargs = request.query_params
    return {"client_host": client_host, "item_id": request_id, "kwargs": kwargs}


query_params = {
    "name": (str, "me"),
    "xxx": (str, "xxx"),
}
query_model = create_model("Query", **query_params)


@router.get("/request/{request_id}/depends")
def read_root(request_id: str, params: query_model = Depends()):
    params_as_dict = params.dict()
    return {"item_id": request_id, "params_as_dict": params_as_dict}
