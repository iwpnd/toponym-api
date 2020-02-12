from starlette.status import HTTP_200_OK


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == HTTP_200_OK
