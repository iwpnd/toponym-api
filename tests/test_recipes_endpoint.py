import json

import pytest
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_404_NOT_FOUND
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
    assert response.status_code == HTTP_200_OK


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_recipes_language_route_valid_json(test_app, language):
    response = test_app.get(API_V1_STR + f"/recipes/{language}")
    assert is_json(response.content)


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_recipes_language_route_default_in_json(test_app, language):
    response = test_app.get(API_V1_STR + f"/recipes/{language}")
    assert "_default" in response.json()["recipes"]


def test_recipes_language_route_language_fails(test_app):
    language = "test"
    response = test_app.get(API_V1_STR + f"/recipes/{language}")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert f"Language: {language} not found" in response.json()["detail"]


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_language_ending_route_status(test_app, language):
    response = test_app.get(API_V1_STR + f"/recipes/{language}/_default")
    assert response.status_code == HTTP_200_OK


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_language_ending_route_response_keys(test_app, language):
    response = test_app.get(API_V1_STR + f"/recipes/{language}/_default")
    assert all([k in response.json() for k in ["language", "ending", "recipe"]])


def test_language_ending_route_language_404(test_app):
    language = "fails"
    response = test_app.get(API_V1_STR + f"/recipes/{language}/_default")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert f"Language: {language} not found" in response.json()["detail"]


def test_language_ending_route_ending_404(test_app):
    response = test_app.get(API_V1_STR + f"/recipes/polish/_test")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert "Ending not found" in response.json()["detail"]


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_recipe_route_status(test_app, language):
    payload = {"language": language, "word": "test"}
    response = test_app.post(API_V1_STR + f"/recipes/recipe", json=payload)
    assert response.status_code == HTTP_200_OK


@pytest.mark.parametrize("language", [language for language in settings.LANGUAGE_DICT])
def test_recipe_route_response(test_app, language):
    payload = {"language": language, "word": "test"}
    response = test_app.post(API_V1_STR + f"/recipes/recipe", json=payload)
    assert all(
        [k in response.json() for k in ["language", "word", "longest_ending", "recipe"]]
    )
