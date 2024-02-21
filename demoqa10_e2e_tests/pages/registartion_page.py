import os
from enum import Enum

import allure

from demoqa10_e2e_tests import resource
from demoqa10_e2e_tests.data.users import User
from selene import browser, be, have


class Hobbies(Enum):
    sport = 'Sports'
    reading = 'Reading'
    music = 'Music'


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.mobile = browser.element('#userNumber')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.button_submit = browser.element("#submit")
        self.close_modal_form = browser.element("#closeLargeModal")

        """
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all("[type=checkbox]")
        self.subjects = browser.element('#subjectsInput')

        """

    def open_page(self):
        with allure.step('Open page'):
            browser.open('/automation-practice-form')
        return self

    def fill_date_of_birth(self, birthday):
        if birthday.day < 10:
            day = '0' + str(birthday.day)
        else:
            day = str(birthday.day)
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{birthday.year}']").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{birthday.month}']").click()
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()
        return self

    def fill_subjects(self, subject: tuple):
        input_value, test_value = subject
        browser.element("#subjectsContainer").click().element('#subjectsInput').type(
            input_value
        )
        browser.all("[id^=react-select-2-option]").element_by(
            have.exact_text(test_value)
        ).click()
        return self

    def hobbies_choose(self, hobbies: list):
        for hobby in hobbies:
            browser.all("[for^='hobbies-checkbox']").element_by(
                have.exact_text(hobby.value)
            ).click()
        return self

    def get_form_table_cells(self):
        return browser.element('.table-responsive').all('td')

    def register(self, user: User):
        with allure.step('Input first name'):
            self.first_name.should(be.blank).type(user.first_name)
        with allure.step('Input last name'):
            self.last_name.should(be.blank).type(user.last_name)
        with allure.step('Input email'):
            self.email.should(be.blank).type(user.email)
        with allure.step('Select gender'):
            self.gender.element_by(have.exact_text(user.gender)).click()
        with allure.step('Input mobile'):
            self.mobile.should(be.blank).type(user.mobile)
        with allure.step('Input date of birth'):
            self.fill_date_of_birth(user.date_of_birth)
        with allure.step('Select subjects'):
            self.fill_subjects(user.subjects)
        with allure.step('Select hobbies'):
            self.hobbies_choose(user.hobbies)
        with allure.step('Select picture'):
            self.picture.send_keys(resource.path(user.picture))
        with allure.step('Type address'):
            self.current_address.should(be.blank).type(user.address)
        with allure.step('Select state'):
            self.state.click()
            browser.all("[id^='react-select-3-option']").element_by(
                have.exact_text(user.state)
            ).click()
        with allure.step('Select city'):
            self.city.click()
            browser.all('[id^=react-select-4-option]').element_by(
                have.exact_text(user.city)
            ).click()
        with allure.step('Press button submit form'):
            self.button_submit.submit()
        # with allure.step('Close modal window'):
        #     self.close_modal_form.click()

        return self
