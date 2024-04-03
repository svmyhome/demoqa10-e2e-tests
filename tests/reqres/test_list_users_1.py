import json
import pytest
from allure_commons._allure import step
from requests import Response
from jsonschema import validate
from demoqa10_e2e_tests.utils.resource import relative_from_root
from demoqa10_e2e_tests.utils.step_logging import request_get_step_logging, response_logging
from tests.schemas import reqres_schemas


USERS_API = 'users'


# @allure.story("List Users")
# class TestListUsers:

@pytest.mark.positive
def test_list_users_get(base_url):
    schema = reqres_schemas.list_users

    response: Response = response_logging(url=f'{base_url}{USERS_API}', method='GET', params={"page": 2})

    with step('Assert response'):
        assert response.status_code == 200
        validate(response.json(), schema)


@pytest.mark.positive
def test_list_users_with_json_get(base_url):
    file_path = relative_from_root('tests/schemas/list_users.json')
    with open(file_path) as file:
        file = json.load(file)

    response: Response = response_logging(url=f'{base_url}{USERS_API}',  method='GET', params={"page": 2})

    with step('Assert response'):
        assert response.status_code == 200
        validate(response.json(), file)


@pytest.mark.negative
def test_list_user_not_found_get(base_url):
    schema = reqres_schemas.user_not_found

    response: Response = response_logging(url=f'{base_url}{USERS_API}/232', method='GET')

    with step('Assert response'):
        assert response.status_code == 404
        validate(response.json(), schema)
