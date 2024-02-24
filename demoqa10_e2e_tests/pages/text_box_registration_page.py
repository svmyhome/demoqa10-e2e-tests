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

    def fill_fullname(self, value):
        self.full_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def fill_permanent_address(self, value):
        self.permanent_address.type(value)
        return self

    def fill_form(self, user: SimpleUser):
        browser.element('#userName').type(user.full_name)
        browser.element('#userEmail').type(user.email)
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#permanentAddress').type(user.permanent_address)
        browser.element('#submit').click()

    def fill(self, simple_user: SimpleUser):
        self.full_name.type(simple_user.full_name)
        self.email.type(simple_user.email)
        self.current_address.type(simple_user.current_address)
        self.permanent_address.type(simple_user.permanent_address)
        self.submit_button.click()
        return self
