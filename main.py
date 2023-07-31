from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import jwt

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Decode(BaseModel):
    token: str
    secret: str

@app.post('/decode')
def root(decode: Decode):
    return jwt.decode(decode.token, decode.secret, algorithms='HS256')

@app.get('/item/{item_id}')
def item(item_id: int):
    return {'item_id': item_id}
