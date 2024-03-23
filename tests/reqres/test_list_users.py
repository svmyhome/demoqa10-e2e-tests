import json
import requests
import pytest
from requests import Response
from jsonschema import validate
from demoqa10_e2e_tests.utils.resource import relative_from_root
from schemas import reqres_schemas


@pytest.mark.positive
def test_list_users_get(base_url):
    schema = reqres_schemas.list_users

    response: Response = requests.get(f'{base_url}users', params={"page": 2})

    assert response.status_code == 200
    validate(response.json(), schema)
    assert response.json()['data'][0]['id'] == 7
    assert response.json()['data'][0]['first_name'] == 'Michael'


@pytest.mark.negative
def test_list_user_not_found_get(base_url):
    schema = reqres_schemas.user_not_found

    response: Response = requests.get(f'{base_url}users/2322')

    assert response.status_code == 404
    validate(response.json(), schema)
    assert response.json() == {}
