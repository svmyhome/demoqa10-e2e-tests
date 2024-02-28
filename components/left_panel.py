import allure
from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.left_panel = browser.element('.element-group')
        self.text_box_form = browser.element('.menu-list').all('li')

    @allure.step('Open form {name_form}')
    def open(self, name_form):
        browser.open('/forms')
        self.left_panel.click()
        self.text_box_form.element_by(have.exact_text(name_form)).click()
        return self

    @allure.step('Open Text Box form via the left menu')
    def open_simple_registration_form(self):
        self.open('Text Box')
