from datetime import date, datetime, time, timedelta
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


'''
declaring paths

path_operation_decorator.operation(path)
path_operation_function

'''


@app.get('/')
@app.get('/exhibitions')
def index(limit: int | None = None, active: bool | None = False, sort: Optional[str] = None):
    return {'exhibitions': 'exhibition_list'}


@app.get('/exhibition/{exhibition_id}')
def about(exhibition_id : int):
    return {'data': {
        'exhibition_id': exhibition_id,
        'exhibition_title': 'exhibition title',
        'datatime': 'time',
        'available_tickets': 'number_of_tickets',
        'customer_list': {
            '1234',
            '3456'
        }
    }}


class Exhibition(BaseModel):
    exhibition_title: str = None
    exhibition_datetime: datetime = None
    available_tickets: int = None


@app.post('/exhibitions')
def create_exhibition(exhibition: Exhibition):
    return f'exhibiton {exhibition.exhibition_title} is created with {exhibition.available_tickets} tickets'

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', post=900)