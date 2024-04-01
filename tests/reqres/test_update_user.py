import pytest
from allure_commons._allure import step
from requests import Response
from jsonschema import validate

from demoqa10_e2e_tests.utils.step_logging import request_put_step_logging, request_patch_step_logging
from tests.schemas import reqres_schemas


@pytest.mark.positive
def test_update_user_put(base_url):
    schema = reqres_schemas.update_user
    payload = {"name": "morpheus1", "job": "leader1"}

    response: Response = request_put_step_logging(f'{base_url}users/2', json=payload)

    with step('Assert response'):
        assert response.status_code == 200
        validate(response.json(), schema)


@pytest.mark.positive
def test_update_user_patch(base_url):
    schema = reqres_schemas.update_user_patch
    payload = {"name": "morpheus1", "job": "leader1"}
    payload_patch = {"name": "morpheus1", "job1": "leader1"}

    response: Response = request_put_step_logging(f'{base_url}users/2', json=payload)

    response: Response = request_patch_step_logging(f'{base_url}users/2', json=payload_patch)

    with step('Assert response'):
        assert response.status_code == 200
        validate(response.json(), schema)
