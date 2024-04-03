import os

import requests
from allure_commons._allure import step
from requests import Response
from selene import browser, have

from demoqa10_e2e_tests.utils import support_methods, data
from demoqa10_e2e_tests.utils.step_logging import request_post_step_logging, response_logging
from demoqa10_e2e_tests.utils.support_methods import clear_cart


def test_login_web():
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    WEB_URL = os.getenv('WEB_URL')

    with step(f'Open {WEB_URL}/login'):
        browser.open(f'{WEB_URL}/login')

    with step('Fill login form'):
        browser.element('#Email').type(LOGIN)
        browser.element('#Password').type(PASSWORD)

    with step("Submit"):
        browser.element('.login-button').click()

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_login_api():
    LOGIN = os.getenv('LOGIN')
    # PASSWORD = os.getenv('PASSWORD')
    WEB_URL = os.getenv('WEB_URL')
    # API_URL = os.getenv('API_URL')
    #
    # payload = {"Email": LOGIN, "Password": PASSWORD}
    # with step('Get cookies'):
    #     response: Response = request_post_step_logging(
    #         url=API_URL, data=payload, allow_redirects=False
    #     )
    #     auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    auth_cookie = support_methods.get_authorize_cookie()

    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(WEB_URL)

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_add_laptop_to_cart():
    LOGIN = os.getenv('LOGIN')
    # PASSWORD = os.getenv('PASSWORD')
    WEB_URL = os.getenv('WEB_URL')
    # API_URL = os.getenv('API_URL')
    add_item = f"{WEB_URL}{data.catalog}/{data.laptop}"
    # payload = {"Email": LOGIN, "Password": PASSWORD}
    #
    # with step('Get cookies'):
    #     response: Response = request_post_step_logging(
    #         url=API_URL, data=payload, allow_redirects=False
    #     )
    #     auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    auth_cookie = support_methods.get_authorize_cookie()

    with step('Add item'):
        request_post_step_logging(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
        )
    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(f'{WEB_URL}cart')
    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))

    clear_cart()

def test_add_laptop_to_cart_1():
    WEB_URL = os.getenv('WEB_URL')
    add_item = f"{WEB_URL}{data.catalog}/{data.laptop}"

    with step('Get authorize cookie'):
        auth_cookie = support_methods.get_authorize_cookie()

    with step('Add item'):
        response_logging(
            url=add_item, method='POST',
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
        )
    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(f'{WEB_URL}cart')
    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))

    clear_cart()




def test_add_gift_card_to_cart():
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    WEB_URL = os.getenv('WEB_URL')
    API_URL = os.getenv('API_URL')
    add_item = f"{WEB_URL}{data.details}/{data.cart}"
    cart_payload = data.cart_payload
    # payload = {"Email": LOGIN, "Password": PASSWORD}
    #
    # with step('Get cookies'):
    #     response: Response = request_post_step_logging(
    #         url=API_URL, data=payload, allow_redirects=False
    #     )
    #     auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with step('Get authorize cookie'):
        auth_cookie = support_methods.get_authorize_cookie()

    with step('Add item'):
        request_post_step_logging(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=cart_payload,
        )
    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(f'{WEB_URL}/cart')
    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))

    clear_cart()


def test_add_desktop_to_cart():
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    WEB_URL = os.getenv('WEB_URL')
    API_URL = os.getenv('API_URL')
    add_item = f"{WEB_URL}{data.details}/{data.desktop}"
    desktop_payload = data.desktop_payload
    # payload = {"Email": LOGIN, "Password": PASSWORD}

    # with step('Open login page'):
    #     response: Response = request_post_step_logging(
    #         url=API_URL, data=payload, allow_redirects=False
    #     )
    #     print(response.status_code)
    #     print(response.headers)
    #     auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    with step('Get authorize cookie'):
        auth_cookie = support_methods.get_authorize_cookie()

    with step('Add item'):
        request_post_step_logging(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=desktop_payload,
        )
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        browser.open(f'{WEB_URL}cart')

    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))

    clear_cart()
