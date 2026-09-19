from fastapi import FastAPI
app=FastAPI()
from pydantic import BaseModel

'''class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create-user")
def create_user(user:User):
    return{
        "Message":"User created",
        "data":user
    }'''

#NESTED MODELS
class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create-user")
def create_user(user:User):
    return user
