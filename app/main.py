from fastapi import FastAPI
from .api import api_users, api_items, api_query_parameters

app = FastAPI()


app.include_router(api_users.router, prefix='/users')
app.include_router(api_items.router, prefix='/items')
app.include_router(api_query_parameters.router, prefix='/query-parameters')


@app.get("/")
def read_root():
    return {"Hello": "World"}
