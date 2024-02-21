import allure
from selene import browser, be, have

from demoqa10_e2e_tests import resource


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    @allure.step('Open automation practice form')
    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    @allure.step('Input first name {value}')
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    @allure.step('Input last name {value}')
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    @allure.step('Input email {value}')
    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    @allure.step('Select gender {value}')
    def gender_choose(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()
        return self

    @allure.step('Input mobile number {value}')
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

    @allure.step('Input subjects {value}')
    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    @allure.step('Select hobbies')
    def hobbies_choose(self, *args):
        for value in args:
            browser.all("[for^='hobbies-checkbox']").element_by(
                have.exact_text(value)
            ).click()
        return self

    @allure.step('Upload picture with name {value}')
    def select_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))
        return self

    @allure.step('Input current address {value}')
    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    @allure.step('Select state {value}')
    def state_choose(self, value):
        self.state.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    @allure.step('Select city {value}')
    def city_choose(self, value):
        self.city.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    @allure.step('Confirm form')
    def submit(self):
        browser.element('#submit').click()
        return self

    @allure.step('Assert registration form')
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

    @allure.step('Close modal window')
    def close_submiting_form(self):
        browser.element("#closeLargeModal").double_click()

    def get_form_table_cells(self):
        return browser.element('.table-responsive').all('td')
