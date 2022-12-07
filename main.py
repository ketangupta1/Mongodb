from fastapi import FastAPI
import db
from modals import *

app = FastAPI()

@app.get("/")
async def hello():
    return {"msg":"Hello World"}

@app.get("/all")
async def get_all():
    data = db.all()
    return {"data":data}

@app.post("/create")
async def create(data:ToDo):
    id = db.create(data)
    return {"Inserted":True, "Id":id}

@app.get("/one")
def get_one(name):
    res = db.get_one(name)
    return {"Result":res}

@app.delete("/delete")
def delete(name):
    res = db.delete(name)
    return {"Delete Status":res}

@app.put("/update")
def update(data:ToDo):
    res = db.update(data)
    return {"Update_Status":True,"Update_Count":res}