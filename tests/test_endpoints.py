VALID_ROW = {
    "date": "2026-10-15",
    "production_line": "Line-A",
    "shift": "Morning",
    "units_planned": 500,
    "units_produced": 480,
    "defective_units": 12,
    "downtime_minutes": 20,
}


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, from backend"}


def test_get_app_name(client):
    response = client.get("/app-name")
    assert response.status_code == 200
    assert response.json() == {"message": "Production prototype app"}


def test_echo_message(client):
    response = client.post("/echo", json={"text": "hello from test"})
    assert response.status_code == 200
    assert response.json() == {"message": "You sent: hello from test"}


def test_echo_message_missing_field_returns_422(client):
    response = client.post("/echo", json={})
    assert response.status_code == 422


def test_insert_row_with_valid_data(client):
    response = client.post("/table", json=[VALID_ROW])
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "Success"


def test_insert_row_with_empty_list_returns_400(client):
    response = client.post("/table", json=[])
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()


def test_insert_row_with_invalid_row_returns_422(client):
    bad_row = {**VALID_ROW, "shift": "x"}  # below min_length=4
    response = client.post("/table", json=[bad_row])
    assert response.status_code == 422
