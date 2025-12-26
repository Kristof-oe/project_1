from fastapi.testclient import TestClient
from main import app

m = TestClient(app)

def test_health():
    response = m.get("/health")
    assert response.status_code == 200
