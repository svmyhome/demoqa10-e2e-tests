import os

import dotenv
import pytest
import requests
from allure_commons._allure import step
from requests import Response
from selene import browser

from demoqa10_e2e_tests.utils import support_methods
from demoqa10_e2e_tests.utils.resource import relative_from_root


@pytest.fixture(scope='session')
def base_url():
    dotenv.load_dotenv()
    return os.getenv("BASE_URL")


@pytest.fixture(scope='session', autouse=True)
def api_setting():
    dotenv.load_dotenv(relative_from_root('.env.local'))


@pytest.fixture(scope='session')
def set_configuration():
    web_url = os.getenv('WEB_URL')

    with step('Get authorize cookie'):
        auth_cookie = support_methods.get_authorize_cookie()
    with step('Browser configuration'):
        browser.config.window_width = 1800
        browser.open(web_url)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})

    browser.open(web_url)

    yield browser

    browser.quit()
