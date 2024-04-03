import os

import allure
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
def set_browser():
    dotenv.load_dotenv(relative_from_root('.env.local'))
    with allure.step('Browser config'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    with allure.step('Add authorization cookie'):
        support_methods.get_authorize_cookie()
        support_methods.set_auth_cookie()

    yield browser

    with allure.step('Close browser'):
        browser.quit()
