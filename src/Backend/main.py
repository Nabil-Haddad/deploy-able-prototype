# import the fastapi class
from contextlib import asynccontextmanager
from fastapi import FastAPI
# import the router from endpoints
from api.endpoints import router as api_router
from db.database import Base, engine
# import models so they register their tables on Base.metadata before create_all runs
from models import model

# create all tables that don't exist yet, at startup rather than import time,
# so importing this module (e.g. in tests) never opens a real DB connection
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

# create the application object
app = FastAPI(lifespan=lifespan)

# include the routes from the api folder
app.include_router(api_router)


# decorator to specify https request type and url
@app.get("/")
def read_root():    # function that handles the request
    return {"message" : "Hello, from backend"} # response