from selene import browser, have
import allure


class CartPage:

    @staticmethod
    def check_item_in_cart(item):
        with allure.step(f'Check item {item} in cart'):
            browser.element('.product-name').should(have.text(item))

    @staticmethod
    def clean_cart():
        with allure.step('Clean cart'):
            browser.all('.qty-input').first.set_value(0)
            browser.element('.update-cart-button').click()


cart_page = CartPage()
