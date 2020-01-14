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
        assert is_json(response.status_code)
