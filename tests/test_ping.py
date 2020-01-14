from starlette.testclient import TestClient

from toponym_api.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
