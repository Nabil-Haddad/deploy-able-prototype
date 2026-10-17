import pytest
from fastapi import HTTPException

from schemas.schema import Rows
from models.model import ProductionModel
from repositories.repository import save_rows_database

VALID_ROW = Rows(
    date="2026-10-15",
    production_line="Line-A",
    shift="Morning",
    units_planned=500,
    units_produced=480,
    defective_units=12,
    downtime_minutes=20,
)


def test_save_rows_database_inserts_and_commits(db_session):
    result = save_rows_database([VALID_ROW], db_session)

    assert result["status"] == "Success"
    stored = db_session.query(ProductionModel).all()
    assert len(stored) == 1
    assert stored[0].production_line == "Line-A"
    assert stored[0].units_produced == 480


def test_save_rows_database_inserts_multiple_rows(db_session):
    second_row = VALID_ROW.model_copy(update={"production_line": "Line-B"})
    save_rows_database([VALID_ROW, second_row], db_session)

    stored = db_session.query(ProductionModel).all()
    assert len(stored) == 2


def test_save_rows_database_rolls_back_on_failure(db_session, monkeypatch):
    def explode():
        raise RuntimeError("simulated DB failure")

    monkeypatch.setattr(db_session, "commit", explode)

    with pytest.raises(HTTPException) as exc_info:
        save_rows_database([VALID_ROW], db_session)

    assert exc_info.value.status_code == 500
    # nothing should have been persisted since commit never succeeded
    assert db_session.query(ProductionModel).count() == 0
