import os
import datetime
from enum import Enum
from demoqa10_e2e_tests.data.user import User
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

    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    # def fill_first_name(self, value):
    #     browser.element('#firstName').should(be.blank).type(value)
    #     return self
    #
    # def fill_last_name(self, value):
    #     browser.element('#lastName').should(be.blank).type(value)
    #     return self
    #
    # def fill_email(self, value):
    #     browser.element('#userEmail').should(be.blank).type(value)
    #     return self

    # def gender_choose(self, value):
    #     browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()
    #     return self

    # def fill_mobile(self, value):
    #     browser.element('#userNumber').should(be.blank).type(value)
    #     return self

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

    # def select_picture(self, path):
    #     browser.element('#uploadPicture').send_keys(os.path.abspath(path))
    #     return self

    # def fill_current_address(self, adress):
    #     browser.element('#currentAddress').should(be.blank).type(adress)
    #     return self

    # def state_choose(self, value):
    #     self.state.click()
    #     browser.all("[id^='react-select-3-option']").element_by(
    #         have.exact_text(value)
    #     ).click()
    #     return self
    #
    # def city_choose(self, value):
    #     self.city.click()
    #     browser.all('[id^=react-select-4-option]').element_by(
    #         have.exact_text(value)
    #     ).click()
    #     return self

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

    def register(
        self,
        first_name,
        last_name,
        email,
        gender,
        mobile,
        birthday,
        subjects,
        hobbies: list,
        picture,
        address,
        state,
        city,
    ):
        self.first_name.should(be.blank).type(first_name)
        self.last_name.should(be.blank).type(last_name)
        self.email.should(be.blank).type(email)
        self.gender.element_by(have.exact_text(gender)).click()
        self.mobile.should(be.blank).type(mobile)
        self.fill_date_of_birth(birthday)
        self.fill_subjects(subjects)
        self.hobbies_choose(hobbies)
        self.picture.send_keys(os.path.abspath(f'../{picture}'))
        self.current_address.should(be.blank).type(address)
        self.state.click()
        browser.all("[id^='react-select-3-option']").element_by(
            have.exact_text(state)
        ).click()

        self.city.click()
        browser.all('[id^=react-select-4-option]').element_by(
            have.exact_text(city)
        ).click()

        return self


if __name__ == '__main__':
    user = User(
        'Ivan',
        'Petrov',
        'qaz@mail.ru',
        'Male',
        '0123456789',
        datetime.date(2019, 8, 1),
        ('p', 'Physics'),
        [Hobbies.sport, Hobbies.reading, Hobbies.music],
        'README.md',
        'SPB, lenina 10',
        'Uttar Pradesh',
        'Lucknow',
    )
    print(user)
    # class Weapon(Enum):
    #     SWORD = 1
    #     BOW = 2
    #     DAGGER = 3
    #     CLUB = 4
    #
    #
    # ranged_weapon = Weapon.BOW
    # print(ranged_weapon)
    #
    # if ranged_weapon == Weapon.BOW:
    #     print("It's a bow")
    #
    # print(list(Weapon))
    #
    # weapon = Weapon.SWORD
    #
    # print(weapon)
    # print(isinstance(weapon, Weapon))
    # print(type(weapon))
    # print(repr(weapon))
    #
    # print(Weapon['SWORD'])
    # print(Weapon(1))

    # birthday = datetime.date(2019, 8, 1)
    # print(birthday)
    # if birthday.day < 10:
    #     day = '0' + str(birthday.day)
    # else:
    #     day = str(birthday.day)
    # print(day)
