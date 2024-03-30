import time

import allure
import requests
from allure_commons._allure import step
from requests import Response
from selene import browser, have

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/login"


def test_login_web():
    with step('Open login page'):
        browser.open(f'{WEB_URL}/login')

    with step('Fill login form'):
        browser.element('#Email').type('example1200@example.com')
        browser.element('#Password').type('123456')

    with step("Submit"):
        browser.element('.login-button').click()

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text(LOGIN))


def test_login_api():
    with step('Open login page'):
        payload = {"Email": LOGIN, "Password": PASSWORD}
        response: Response = requests.post(
            url=API_URL, data=payload, allow_redirects=False
        )
        print(response.status_code)
        print(response.headers)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorize"):
        browser.element('.account').should(have.text('example1200@example.com'))


def test_add_laptop_to_cart():
    add_item = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"
    with step('Open login page'):
        payload = {"Email": LOGIN, "Password": PASSWORD}
        response: Response = requests.post(
            url=API_URL, data=payload, allow_redirects=False
        )
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
        )
    browser.open(WEB_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    browser.open('https://demowebshop.tricentis.com/cart')
    with step('Verify input value'):
        browser.all('.qty-input').first.should(have.value('1'))
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()
    # [name='itemquantity4124532']
    # with step("Verify successful authorize"):
    #     browser.element('.account').should(have.text('example1200@example.com'))


def test_add_gift_card_to_cart():
    add_item = "https://demowebshop.tricentis.com/addproducttocart/details/2/1"
    payload_1 = {
        "giftcard_2.RecipientName": "rwerewrwe@mail.ru",
        "giftcard_2.RecipientEmail": "rwerewrwe@mail.ru",
        "giftcard_2.SenderName": "Exam+Ple",
        "giftcard_2.SenderEmail": "example1200@example.com",
        "giftcard_2.Message": "Fuck off",
        "addtocart_2.EnteredQuantity": 1,
    }

    with step('Open login page'):
        payload = {"Email": LOGIN, "Password": PASSWORD}
        response: Response = requests.post(
            url=API_URL, data=payload, allow_redirects=False
        )
        print(response.status_code)
        print(response.headers)
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=payload_1,
        )
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        browser.open('https://demowebshop.tricentis.com/cart')
        with step('Verify input value'):
            browser.all('.qty-input').first.should(have.value('1'))
        with step('Clear the cart'):
            browser.all('.qty-input').first.set_value(0)
            browser.element('.update-cart-button').click()


def test_add_desktop_to_cart():
    add_item = "https://demowebshop.tricentis.com/addproducttocart/details/72/1"
    payload_1 = {
        "product_attribute_72_5_18": 53,
        "product_attribute_72_6_19": 54,
        "product_attribute_72_3_20": 57,
        "product_attribute_72_8_30": 93,
        "addtocart_72.EnteredQuantity": 1,
    }

    with step('Open login page'):
        payload = {"Email": LOGIN, "Password": PASSWORD}
        response: Response = requests.post(
            url=API_URL, data=payload, allow_redirects=False
        )
        print(response.status_code)
        print(response.headers)
        auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        requests.post(
            url=add_item,
            cookies={"NOPCOMMERCE.AUTH": auth_cookie},
            data=payload_1,
        )
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
        browser.open('https://demowebshop.tricentis.com/cart')
        with step('Verify input value'):
            browser.all('.qty-input').first.should(have.value('1'))
        with step('Clear the cart'):
            browser.all('.qty-input').first.set_value(0)
            browser.element('.update-cart-button').click()
