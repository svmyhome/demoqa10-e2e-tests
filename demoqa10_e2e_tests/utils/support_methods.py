from allure_commons._allure import step
from selene import browser


def clear_cart():
    with step('Clear the cart'):
        browser.all('.qty-input').first.set_value(0)
        browser.element('.update-cart-button').click()