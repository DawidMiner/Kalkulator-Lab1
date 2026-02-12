from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_addition():
    response = client.post("/api/calculate", json={"num1": 2, "num2": 3, "operator": "+"})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_division_by_zero():
    response = client.post("/api/calculate", json={"num1": 10, "num2": 0, "operator": "/"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Nie można dzielić przez zero"