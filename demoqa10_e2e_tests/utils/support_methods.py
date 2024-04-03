import os

import dotenv
from requests import Response
from selene import browser

from demoqa10_e2e_tests.utils.resource import relative_from_root
from demoqa10_e2e_tests.utils.step_logging import response_logging



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


def set_auth_cookie():
    dotenv.load_dotenv(relative_from_root('.env.local'))
    url_web = os.getenv('WEB_URL')
    browser.open(url_web)
    browser.driver.add_cookie(
        {'name': "NOPCOMMERCE.AUTH", 'value': get_authorize_cookie()}
    )
    browser.open(url_web)
