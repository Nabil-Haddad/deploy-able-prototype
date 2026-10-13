from fastapi import APIRouter
from pydantic import BaseModel



# create the post message model
class EchoRequest(BaseModel):
    text : str

# Initialise the router to connect back to main.py
router = APIRouter()


@router.get("/app-name")
def get_app_name():
    return {"message": "Production prototype app"}

@router.post("/echo")
def echo_message(payload:EchoRequest):
    return {"message": f"You sent: {payload.text}"}