from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:int

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name":"Poo",
            "age":22,
                "password":123456    }
