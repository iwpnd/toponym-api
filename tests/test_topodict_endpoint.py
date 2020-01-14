from starlette.testclient import TestClient
from toponym_api.main import app
from toponym_api.core.config import API_V1_STR
from toponym import settings
import json


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


client = TestClient(app)

available_languages = [entry for entry in settings.LANGUAGE_DICT]


def test_topodict_language_route():
    for language in available_languages:
        response = client.get(API_V1_STR + f"/topodict/{language}")
        assert response.status_code == 200


def test_topodict_language_route_valid_json():
    for language in available_languages:
        response = client.get(API_V1_STR + f"/topodict/{language}")
        assert is_json(response.content)


def test_topodict_language_route_default_in_json():
    for language in available_languages:
        response = client.get(API_V1_STR + f"/topodict/{language}")
        assert "_default" in response.json()["topodictionary"]


def test_topodict_language_route_language_fails():
    language = "test"
    response = client.get(API_V1_STR + f"/topodict/{language}")
    assert response.status_code == 404
    assert f"Language: {language} not found" in response.json()["detail"]


def test_language_ending_route_status():
    for language in available_languages:
        response = client.get(API_V1_STR + f"/topodict/{language}/_default")
        assert response.status_code == 200


def test_language_ending_route_response_keys():
    for language in available_languages:
        response = client.get(API_V1_STR + f"/topodict/{language}/_default")
        assert all([k in response.json() for k in response.json().keys()])


def test_language_ending_route_language_404():
    language = "test"
    response = client.get(API_V1_STR + f"/topodict/{language}/_default")
    assert response.status_code == 404
    assert f"Language: {language} not found" in response.json()["detail"]


def test_language_ending_route_ending_404():
    response = client.get(API_V1_STR + f"/topodict/polish/_test")
    assert response.status_code == 404
    assert "Ending not found" in response.json()["detail"]


def test_recipe_route_status():
    payload = {"language": "polish", "word": "test"}
    response = client.post(API_V1_STR + f"/topodict/recipe", json=payload)
    assert response.status_code == 200
