from selene import browser, have


class LeftPanel:

    def __init__(self):
        self.first_name = browser.element('#firstName')

    def open(self):
        browser.open('/forms')
        browser.element('.element-group').click()
        browser.element('.accordion .element-list.collapse').click()
        browser.element('.menu-list').all('li').element_by(have.exact_text('Text Box')).click()
        return self


    def open_simple_registration_form(self):
        self.open()

        print()
