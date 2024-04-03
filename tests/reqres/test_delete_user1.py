import pytest
from allure_commons._allure import step
from requests import Response

from demoqa10_e2e_tests.utils.step_logging import request_delete_step_logging, response_logging


@pytest.mark.positive
def test_delete_user(base_url):
    response: Response = response_logging(f'{base_url}users/2', method='DELETE')

    with step('Assert response'):
        assert response.status_code == 204
