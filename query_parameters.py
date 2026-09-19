from fastapi import FastAPI
app=FastAPI()
@app.get("/users")
def get_users(name:str=None):
    return{"name":name}

#default value
@app.get("/products")
def get_products(limit:int=10):
    return{"limit":limit}

#Multiple query parameters
@app.get("/items")
def get_products(name:str=None,price:int=0):
    return{"name":name,
           "price":price}