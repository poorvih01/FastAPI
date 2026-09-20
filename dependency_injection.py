from fastapi import FastAPI,Depends,Header,HTTPException
app=FastAPI()

def verify_token(token:str=Header(None)):
    if token!="mysecret":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "user":"Authorized"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"This is secure data",
        "user":user
    }
    

'''def common_logic():
    return{
        "message":"common logic executed"
    }

@app.get("/home")
def home(data=Depends(common_logic)):
    return data'''

#REUSABLE LOGIC
'''def get_current_user():
    return{
        'user":"Poo'
    }
@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user

@app.get("/dashboard")
def pdashboard(user=Depends(get_current_user)):
    return user'''

