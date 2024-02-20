import os

from selene import browser, be, have


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def gender_choose(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{year}']").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{month}']").click()
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()
        return self

    def fill_subjects(self, value):
        browser.element("#subjectsContainer").click().element('#subjectsInput').type(
            'p'
        )
        browser.all("[id^=react-select-2-option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    def hobbies_choose(self, *args):
        for value in args:
            browser.all("[for^='hobbies-checkbox']").element_by(
                have.exact_text(value)
            ).click()
        return self

    def select_picture(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))
        return self

    def fill_current_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)
        return self

    def state_choose(self, value):
        self.state.click()
        browser.all("[id^='react-select-3-option']").element_by(
            have.exact_text(value)
        ).click()
        return self

    def city_choose(self, value):
        self.city.click()
        browser.all('[id^=react-select-4-option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def assert_fill_form(
        self,
        name,
        email,
        gender,
        mobile,
        birthday,
        subjects,
        hobbies,
        picture,
        address,
        state_city,
    ):
        browser.element('.table-responsive').all('tbody>tr').should(
            have.exact_texts(
                name,
                email,
                gender,
                mobile,
                birthday,
                subjects,
                hobbies,
                picture,
                address,
                state_city,
            )
        )

    def get_form_table_cells(self):
        return browser.element('.table-responsive').all('td')
