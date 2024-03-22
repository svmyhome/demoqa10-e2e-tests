import requests
import pytest
from requests import Response
from jsonschema import validate

from tests.schemas import reqres_schemas


@pytest.mark.negative
def test_register_user_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"password": "sydney@fife"}

    response: Response = requests.post(f'{base_url}register', json=payload)
    print(response.text)

    assert response.status_code == 400
    validate(response.json(), schema)


@pytest.mark.negative
def test_register_user_without_password_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"email": "sydney@fife"}

    response: Response = requests.post(f'{base_url}register', json=payload)
    print(response.text)

    assert response.status_code == 400
    validate(response.json(), schema)


@pytest.mark.negative
def test_register_user_without_email_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"password": "sydney@fife"}

    response: Response = requests.post(f'{base_url}register', json=payload)
    print(response.text)

    assert response.status_code == 400
    validate(response.json(), schema)
