from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_connect = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_connect.incr('test:increment',1)
    return {"Counter": counter}

#路徑參數
@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_connect.incr('test:increment',c)
    return{"Counter":counter}


@app.get("/items/{item_id}")
def read_item(item_id: int, q:str | None = None):
    return {"item_id": item_id, "q": q}