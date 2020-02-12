import json

from starlette.status import HTTP_200_OK

from toponym_api.core.config import API_V1_STR


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def test_language_route_status(test_app):
    response = test_app.get(API_V1_STR + f"/languages")
    assert response.status_code == HTTP_200_OK


def test_language_route_valid_json(test_app):
    response = test_app.get(API_V1_STR + f"/languages")
    assert is_json(response.content)


def test_language_route_languages(test_app, available_languages):
    response = test_app.get(API_V1_STR + f"/languages")
    assert all([language in response.json() for language in available_languages])
