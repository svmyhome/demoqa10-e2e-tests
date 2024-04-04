import os

import allure


from demoqa10_e2e_tests.api.cart import cart
from demoqa10_e2e_tests.pages.cart_page import cart_page
from demoqa10_e2e_tests.pages.main_page import main_page

from demoqa10_e2e_tests.utils import data


def test_login_api():
    with allure.step('Verify authorization'):
        main_page.check_auth_is_success(os.getenv('LOGIN'))


def test_add_notebook_add_to_cart():
    cart.add_item(data.laptop, data.catalog)
    main_page.go_to_cart()
    cart_page.check_item_in_cart(data.laptop_name)
    cart_page.clean_cart()


def test_add_gift_card_to_cart():
    cart.add_item(data.cart, data.details, data.cart_payload)
    main_page.go_to_cart()
    cart_page.check_item_in_cart(data.cart_name)
    cart_page.clean_cart()


def test_add_desktop_to_cart():
    cart.add_item(data.desktop, data.details, data.desktop_payload)
    main_page.go_to_cart()
    cart_page.check_item_in_cart(data.desktop_name)
    cart_page.clean_cart()
