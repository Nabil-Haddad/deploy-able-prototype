from fastapi import APIRouter, HTTPException
from schemas.schema import EchoRequest,Rows

# Initialise the router to connect back to main.py
router = APIRouter()


@router.get("/app-name")
def get_app_name():
    return {"message": "Production prototype app"}

@router.post("/echo")
def echo_message(payload:EchoRequest):
    return {"message": f"You sent: {payload.text}"}

@router.post("/table")
async def insert_row(rows:list[Rows]):
    try :
        if not rows:
            raise HTTPException(status_code= 400, detail="The row list cannot be empty")
        counter = 0
        for r in rows:
            # save each row to the database
            print(f"The row with the date {r.date} was successfully inserted")
            counter += 1

        return {
            "status" : "Sucesss",
            "message" : f"{counter} rows were inserted with success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insertion failed: {str(e)}")

