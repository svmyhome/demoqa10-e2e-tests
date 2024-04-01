import requests
from allure_commons._allure import step
from requests import Response
from selene import browser, have

from demoqa10_e2e_tests.utils.step_logging import request_post_step_logging

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/login"


def test_login_web():
    with step(f'Open {WEB_URL}/login'):
        browser.open(f'{WEB_URL}/login')

    with step('Fill login form'):
        browser.element('#Email').type('example1200@example.com')
        browser.element('#Password').type('123456')

    with step("Submit"):
        browser.element('.login-button').click()

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_login_api():
    payload = {"Email": LOGIN, "Password": PASSWORD}

    with step('Get cookies'):
        response: Response = request_post_step_logging(
            url=API_URL, data=payload, allow_redirects=False
        )
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    with step('Set cookie to browser'):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    with step("Open authorize page"):
        browser.open(WEB_URL)

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_add_laptop_to_cart():
    add_item = f"{WEB_URL}addproducttocart/catalog/31/1/1"
    payload = {"Email": LOGIN, "Password": PASSWORD}

    with step('Get cookies'):
        response: Response = request_post_step_logging(
            url=API_URL, data=payload, allow_redirects=False
        )
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
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
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()
    # [name='itemquantity4124532']
    # with step("Verify successful authorize"):
    #     browser.element('.account').should(have.text('example1200@example.com'))


def test_add_gift_card_to_cart():
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
        response: Response = request_post_step_logging(
            url=API_URL, data=payload, allow_redirects=False
        )
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    with step('Add item'):
        request_post_step_logging(
            url=add_item,
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
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()


def test_add_desktop_to_cart():
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
        response: Response = request_post_step_logging(
            url=API_URL, data=payload, allow_redirects=False
        )
        print(response.status_code)
        print(response.headers)
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        request_post_step_logging(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=payload_1,
        )
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        browser.open(f'{WEB_URL}cart')

    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()
