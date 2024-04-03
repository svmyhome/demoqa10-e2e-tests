import os

import requests
from allure_commons._allure import step
from requests import Response
from selene import browser, have

from demoqa10_e2e_tests.utils import support_methods
from demoqa10_e2e_tests.utils.step_logging import (
    request_post_step_logging,
    response_logging,
)
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
    WEB_URL = os.getenv('WEB_URL')

    auth_cookie = support_methods.get_authorize_cookie()

    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(WEB_URL)

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_add_laptop_to_cart():
    WEB_URL = os.getenv('WEB_URL')
    add_item = f"{WEB_URL}addproducttocart/catalog/31/1/1"

    with step('Get authorize cookie'):
        auth_cookie = support_methods.get_authorize_cookie()

    with step('Add item'):
        response_logging(
            url=add_item,
            method='POST',
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
    add_item = f"{WEB_URL}addproducttocart/details/2/1"
    payload_1 = {
        "giftcard_2.RecipientName": "rwerewrwe@mail.ru",
        "giftcard_2.RecipientEmail": "rwerewrwe@mail.ru",
        "giftcard_2.SenderName": "Exam+Ple",
        "giftcard_2.SenderEmail": "example1200@example.com",
        "giftcard_2.Message": "Fuck off",
        "addtocart_2.EnteredQuantity": 1,
    }
    payload = {"Email": LOGIN, "Password": PASSWORD}

    with step('Get cookies'):
        response: Response = response_logging(
            url=API_URL, method='POST', data=payload, allow_redirects=False
        )
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    with step('Add item'):
        response_logging(
            url=add_item,
            method='POST',
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=payload_1,
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
    add_item = f"{WEB_URL}addproducttocart/details/72/1"
    payload_1 = {
        "product_attribute_72_5_18": 53,
        "product_attribute_72_6_19": 54,
        "product_attribute_72_3_20": 57,
        "product_attribute_72_8_30": 93,
        "addtocart_72.EnteredQuantity": 1,
    }
    payload = {"Email": LOGIN, "Password": PASSWORD}

    with step('Open login page'):
        response: Response = response_logging(
            url=API_URL, method='POST', data=payload, allow_redirects=False
        )
        print(response.status_code)
        print(response.headers)
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        response_logging(
            url=add_item,
            method='POST',
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=payload_1,
        )
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        browser.open(f'{WEB_URL}cart')

    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))

    clear_cart()
