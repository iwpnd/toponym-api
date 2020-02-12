import json

import pytest
from toponym import settings

from toponym_api.core.config import API_V1_STR


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_recipes_language_route(test_app, language):
    response = test_app.get(API_V1_STR + f"/recipes/{language}")
    assert response.status_code == 200


# def test_topodict_language_route_valid_json():
#     for language in available_languages:
#         response = client.get(API_V1_STR + f"/topodict/{language}")
#         assert is_json(response.content)


# def test_topodict_language_route_default_in_json():
#     for language in available_languages:
#         response = client.get(API_V1_STR + f"/topodict/{language}")
#         assert "_default" in response.json()["topodictionary"]


# def test_topodict_language_route_language_fails():
#     language = "test"
#     response = client.get(API_V1_STR + f"/topodict/{language}")
#     assert response.status_code == 404
#     assert f"Language: {language} not found" in response.json()["detail"]


# def test_language_ending_route_status():
#     for language in available_languages:
#         response = client.get(API_V1_STR + f"/topodict/{language}/_default")
#         assert response.status_code == 200


# def test_language_ending_route_response_keys():
#     for language in available_languages:
#         response = client.get(API_V1_STR + f"/topodict/{language}/_default")
#         assert all([k in response.json() for k in ["language", "ending", "recipe"]])


# def test_language_ending_route_language_404():
#     language = "test"
#     response = client.get(API_V1_STR + f"/topodict/{language}/_default")
#     assert response.status_code == 404
#     assert f"Language: {language} not found" in response.json()["detail"]


# def test_language_ending_route_ending_404():
#     response = client.get(API_V1_STR + f"/topodict/polish/_test")
#     assert response.status_code == 404
#     assert "Ending not found" in response.json()["detail"]


# def test_recipe_route_status():
#     for language in available_languages:
#         payload = {"language": language, "word": "test"}
#         response = client.post(API_V1_STR + f"/topodict/recipe", json=payload)
#         assert response.status_code == 200


# def test_recipe_route_response():
#     for language in available_languages:
#         payload = {"language": language, "word": "test"}
#         response = client.post(API_V1_STR + f"/topodict/recipe", json=payload)
#         assert all(
#             [
#                 k in response.json()
#                 for k in ["language", "word", "longest_ending", "recipe"]
#             ]
#         )
