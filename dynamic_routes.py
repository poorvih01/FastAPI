from fastapi import FastAPI
app=FastAPI()
#HOMEPAGE
@app.get("/")
def home():
    return{"message":"Welcome to FastAPI"}

#ABOUT route
@app.get("/about")
def about():
    return{"message":"This is the about page"}

#USERS route
@app.get("/users/{user_id}")
def get_users(user_id:int):
     return{"user_id":user_id}