import json
import requests
import pytest
from requests import Response
from jsonschema import validate
from demoqa10_e2e_tests.utils.resource import relative_from_root
from tests.schemas import reqres_schemas


@pytest.mark.positive
def test_list_users_get(base_url):
    schema = reqres_schemas.list_users

    response: Response = requests.get(f'{base_url}users', params={"page": 2})
    print(response.text)

    assert response.status_code == 200
    validate(response.json(), schema)


@pytest.mark.positive
def test_list_users_with_json_get(base_url):
    # file_path = relative_from_root('tests/schemas/list_users.json')
    # with open(file_path) as file:
    #     file = json.load(file)

    response: Response = requests.get(f'{base_url}users', params={"page": 2})
    print(response.text)

    assert response.status_code == 200
    validate(response.json(), file)


@pytest.mark.negative
def test_list_user_not_found_get(base_url):
    schema = reqres_schemas.user_not_found

    response: Response = requests.get(f'{base_url}users/2322')
    print(response.text)

    assert response.status_code == 404
    validate(response.json(), schema)
