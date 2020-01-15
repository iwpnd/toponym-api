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


def test_topogen_route_status():
    language = random.choice(available_languages)
    payload = {"language": language, "word": "test"}
    response = client.post(API_V1_STR + "/toponym/", json=payload)
    assert response.status_code == HTTP_200_OK


def test_topogen_route_valid_json():
    language = random.choice(available_languages)
    payload = {"language": language, "word": "test"}
    response = client.post(API_V1_STR + "/toponym/", json=payload)
    assert is_json(response.content)


def test_topogen_route_fails_404():
    language = "failsnail"
    payload = {"language": language, "word": "test"}
    response = client.post(API_V1_STR + "/toponym/", json=payload)
    assert response.status_code == HTTP_404_NOT_FOUND
    assert f"Language: {language} not found" in response.json()["detail"]
