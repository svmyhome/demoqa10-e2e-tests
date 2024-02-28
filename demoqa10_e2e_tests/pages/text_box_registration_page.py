import allure
from selene import browser

from demoqa10_e2e_tests.test_data.users import SimpleUser


class TextBoxRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/text-box')

    def fill(self, simple_user: SimpleUser):
        with allure.step('Fill full name'):
            self.full_name.type(simple_user.full_name)
        with allure.step('Fill Email'):
            self.email.type(simple_user.email)
        with allure.step('Fill current address'):
            self.current_address.type(simple_user.current_address)
        with allure.step('Fill permanent address'):
            self.permanent_address.type(simple_user.permanent_address)
        with allure.step('Submit form'):
            self.submit_button.click()
        return self