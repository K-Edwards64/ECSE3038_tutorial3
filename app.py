from datetime import datetime
from typing import List
import fastapi
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

app = FastAPI()

class Fruit(BaseModel):
    id: UUID = Field(default_factory=uuid4)

    name: str
    variety: str
    quanitity: int
    supplier: str
    harvest_date: datetime
    creation_date: datetime = Field(default_factory= datetime.now)
    available: bool = Field(default=True)
    price: float
    

Basket : List[Fruit] = []



@app.get("/fruits")
async def get_basket():
    for fruit in Basket:
        if fruit.available == True:
            return Fruit

    return{"No Fruits Available"}

@app.get("/spec_fruits/{id}")
async def get_spec_fruit(id: UUID):
    for fruit in Basket:
        if fruit.id == id:
            return Fruit

    return{"Fruit Not Found"}

@app.post("/fruits")
async def add_fruit(new_fruit: Fruit):
    Basket.append(new_fruit)
    fruit_json = jsonable_encoder(new_fruit)
    return fruit_json