from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from toponym_api.main import app
from toponym_api.core.config import API_V1_STR
from toponym import settings
import random
import json


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


client = TestClient(app)

available_languages = [entry for entry in settings.LANGUAGE_DICT]


def test_language_route_status():
    response = client.get(API_V1_STR + f"/languages")
    assert response.status_code == HTTP_200_OK


def test_language_route_valid_json():
    response = client.get(API_V1_STR + f"/languages")
    assert is_json(response.content)


def test_language_route_languages():
    response = client.get(API_V1_STR + f"/languages")
    assert all([language in response.json() for language in available_languages])
