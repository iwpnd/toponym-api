import pytest
from starlette.testclient import TestClient
from toponym import settings

from toponym_api.main import app


@pytest.fixture
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture
def available_languages():
    return (entry for entry in settings.LANGUAGE_DICT)
