from selene import browser, have

import allure


class MainPage:
    @staticmethod
    def check_auth_is_success(login):
        with allure.step('Check authorization'):
            browser.element('.account').should(have.text(login))

    @staticmethod
    def go_to_cart():
        with allure.step('Go to cart page'):
            browser.element('#topcartlink').click()


main_page = MainPage()