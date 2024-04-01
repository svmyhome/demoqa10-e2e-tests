import pytest
from allure_commons._allure import step
from requests import Response
from jsonschema import validate

from demoqa10_e2e_tests.utils.step_logging import request_post_step_logging
from tests.schemas import reqres_schemas


@pytest.mark.negative
def test_register_user_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"password": "sydney@fife"}

    response: Response = request_post_step_logging(f'{base_url}register', json=payload)

    with step('Assert response'):
        assert response.status_code == 400
        validate(response.json(), schema)


@pytest.mark.negative
def test_register_user_without_password_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"email": "sydney@fife"}

    response: Response = request_post_step_logging(f'{base_url}register', json=payload)

    with step('Assert response'):
        assert response.status_code == 400
        validate(response.json(), schema)


@pytest.mark.negative
def test_register_user_without_email_post(base_url):
    schema = reqres_schemas.register_user_fail
    payload = {"password": "sydney@fife"}

    response: Response = request_post_step_logging(f'{base_url}register', json=payload)

    with step('Assert response'):
        assert response.status_code == 400
        validate(response.json(), schema)
