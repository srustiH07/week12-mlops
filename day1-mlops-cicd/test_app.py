from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={"feature": 5},
    )

    assert response.status_code == 200
    assert response.json()["prediction"] == 10.0