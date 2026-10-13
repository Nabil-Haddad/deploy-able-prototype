# import the fastapi class
from fastapi import FastAPI
# import the router from endpoints
from api.endpoints import router as api_router

# create the application object
app = FastAPI()

# include the routes from the api folder
app.include_router(api_router)


# decorator to specify https request type and url
@app.get("/")
def read_root():    # function that handles the request
    return {"message" : "Hello, from backend"} # response