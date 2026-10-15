from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.schema import EchoRequest,Rows
from db.database import get_db
from repositories.repository import save_rows_database

# Initialise the router to connect back to main.py
router = APIRouter()


@router.get("/app-name")
def get_app_name():
    return {"message": "Production prototype app"}

@router.post("/echo")
def echo_message(payload:EchoRequest):
    return {"message": f"You sent: {payload.text}"}

@router.post("/table")
async def insert_row(rows:list[Rows], db: Session = Depends(get_db)):
    if not rows:
        raise HTTPException(status_code= 400, detail="The row list cannot be empty")
    return save_rows_database(rows, db)

