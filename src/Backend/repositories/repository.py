from schemas.schema import Rows
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.model import ProductionModel


def save_rows_database(payload_rows:list[Rows],db:Session):
    try :
        db_production = [
            ProductionModel(
                date=r.date,
                    production_line=r.production_line,
                    shift=r.shift,
                    units_planned=r.units_planned,
                    units_produced=r.units_produced,
                    defective_units=r.defective_units,
                    downtime_minutes=r.downtime_minutes
            )
            for r in payload_rows
        ]

        db.bulk_save_objects(db_production)
        db.commit()

        return {
            "status" : "Success",
            "message" : f"{len(payload_rows)}rows were written successfully. "
        }
    except Exception as e:
        # roll back in the database
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database insertion failed: {str(e)}")