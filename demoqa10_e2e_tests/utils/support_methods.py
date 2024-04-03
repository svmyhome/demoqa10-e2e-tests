import os

import dotenv
import requests
from allure_commons._allure import step
from requests import Response
from selene import browser

from demoqa10_e2e_tests.utils.resource import relative_from_root
from demoqa10_e2e_tests.utils.step_logging import response_logging


@staticmethod
def get_authorize_cookie():
    dotenv.load_dotenv(relative_from_root('.env.local'))
    url_api = os.getenv('API_URL')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    payload = {"Email": login, "Password": password}
    response: Response = response_logging(
        url=url_api,
        method='POST',
        data=payload,
        allow_redirects=False,
    )

    return response.cookies.get("NOPCOMMERCE.AUTH")


@staticmethod
def clear_cart():
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()


print(get_authorize_cookie())
