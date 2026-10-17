import pytest
from pydantic import ValidationError

from schemas.schema import EchoRequest, Rows

VALID_ROW = {
    "date": "2026-10-15",
    "production_line": "Line-A",
    "shift": "Morning",
    "units_planned": 500,
    "units_produced": 480,
    "defective_units": 12,
    "downtime_minutes": 20,
}


def test_echo_request_accepts_a_string():
    req = EchoRequest(text="hello")
    assert req.text == "hello"


def test_echo_request_rejects_missing_field():
    with pytest.raises(ValidationError):
        EchoRequest()


def test_rows_accepts_valid_data():
    row = Rows(**VALID_ROW)
    assert row.production_line == "Line-A"
    assert row.units_produced == 480


@pytest.mark.parametrize("field", ["production_line", "shift"])
def test_rows_rejects_string_below_min_length(field):
    bad_row = {**VALID_ROW, field: "abc"}  # min_length=4
    with pytest.raises(ValidationError):
        Rows(**bad_row)


@pytest.mark.parametrize("field", ["production_line", "shift"])
def test_rows_rejects_string_above_max_length(field):
    bad_row = {**VALID_ROW, field: "x" * 21}  # max_length=20
    with pytest.raises(ValidationError):
        Rows(**bad_row)


def test_rows_rejects_non_integer_units():
    bad_row = {**VALID_ROW, "units_produced": "not-a-number"}
    with pytest.raises(ValidationError):
        Rows(**bad_row)


def test_rows_rejects_invalid_date():
    bad_row = {**VALID_ROW, "date": "not-a-date"}
    with pytest.raises(ValidationError):
        Rows(**bad_row)


def test_rows_rejects_missing_required_field():
    incomplete_row = {k: v for k, v in VALID_ROW.items() if k != "shift"}
    with pytest.raises(ValidationError):
        Rows(**incomplete_row)
