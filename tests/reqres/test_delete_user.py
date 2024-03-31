import pytest
from allure_commons._allure import step
from requests import Response

from demoqa10_e2e_tests.utils.step_logging import reqres_delete_step_logging


@pytest.mark.positive
def test_delete_user(base_url):
    response: Response = reqres_delete_step_logging(f'{base_url}users/2')

    with step('Assert response'):
        assert response.status_code == 204
