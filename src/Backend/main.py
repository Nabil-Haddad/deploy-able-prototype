# import the fastapi class
from fastapi import FastAPI

# create the application object
app = FastAPI()

# decorator to specify https request type and url
@app.get("/")
def read_root():    # function that handles the request
    return {"message" : "Hello, from backend"} # response