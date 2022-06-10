from typing import Union

from fastapi import FastAPI
from .api import api_users, api_items

app = FastAPI()


app.include_router(api_users.router, prefix='/users')
app.include_router(api_items.router, prefix='/items')


@app.get("/")
def read_root():
    return {"Hello": "World"}
