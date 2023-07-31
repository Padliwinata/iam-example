from fastapi import FastAPI
from pydantic import BaseModel
from jose import jwt

app = FastAPI()

class Decode(BaseModel):
    token: str
    secret: str

@app.post('/decode')
def root(decode: Decode):
    return jwt.decode(decode.token, decode.secret, algorithms='HS256')

@app.get('/item/{item_id}')
def item(item_id: int):
    return {'item_id': item_id}
