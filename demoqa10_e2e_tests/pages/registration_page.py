from enum import Enum
import allure
from selenium.webdriver import Keys

from demoqa10_e2e_tests.utils import resource
from demoqa10_e2e_tests.test_data.users import User
from selene import browser, be, have
from demoqa10_e2e_tests.utils.user_data_processing import get_hobbies


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.mobile = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.button_submit = browser.element("#submit")
        self.close_modal_form = browser.element("#closeLargeModal")

    def open_page(self):
        with allure.step('Open page'):
            browser.open('/automation-practice-form')
        return self

    def fill_date_of_birth(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").send_keys(
            user.date_of_birth_year
        )
        browser.element(".react-datepicker__month-select").send_keys(
            user.date_of_birth_month
        )
        browser.element(f".react-datepicker__day--0{user.date_of_birth_day}").click()
        return self

    @allure.step('Select hobbies')
    def hobbies_choose(self, hobbies: list[Enum]):
        for hobby in hobbies:
            browser.all("[for^='hobbies-checkbox']").element_by(
                have.exact_text(hobby.value)
            ).click()
        return self

    @allure.step('Select state')
    def fill_state(self, user: User):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.state)
        ).click()

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
            self.fill_date_of_birth(user)
        with allure.step('Select subjects'):
            self.subjects.type(user.subjects).press_enter()
        self.hobbies_choose(user.hobbies)
        with allure.step('Select picture'):
            self.picture.send_keys(resource.path(user.picture))
        with allure.step('Type address'):
            self.current_address.should(be.blank).type(user.current_address)
        self.fill_state(user)
        with allure.step('Select city'):
            self.city.click()
            browser.all('[id^=react-select-4-option]').element_by(
                have.exact_text(user.city)
            ).click()
        with allure.step('Press button submit form'):
            self.button_submit.submit()

        return self

    def should_have_registered_user_with(self, user: User):
        browser.element(".table").all("td:nth-child(2)").should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.mobile,
                f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                user.subjects,
                get_hobbies(user),
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )
