import os

import allure
from allure_commons.types import Severity
from selene import browser, be, have

from demoqa10_e2e_tests.pages.registration_page import RegistrationPage

YEAR = '2019'
MONTH = '8'
DAY = '01'


@allure.tag('DemoQA', 'Проверка внутри Page object')
@allure.feature('Registration Form 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='Practice Form')
def test_fill_practice_form_with_revision(browser_management):
    registration_page = RegistrationPage()

    registration_page.open_page()

    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Petrov')
    registration_page.fill_email('qaz@mail.ru')

    registration_page.gender_choose('Male')

    registration_page.fill_mobile('0123456789')

    registration_page.fill_date_of_birth(YEAR, MONTH, DAY)

    registration_page.fill_subjects('Physics')

    registration_page.hobbies_choose('Sports', 'Reading', 'Music')

    registration_page.select_picture('robo.png')

    registration_page.fill_current_address('SPB, lenina 10')

    registration_page.state_choose('Uttar Pradesh')

    registration_page.city_choose('Lucknow')

    registration_page.submit()

    registration_page.assert_fill_form(
        'Student Name Ivan Petrov',
        'Student Email qaz@mail.ru',
        'Gender Male',
        'Mobile 0123456789',
        'Date of Birth 01 September,2019',
        'Subjects Physics',
        'Hobbies Sports, Reading, Music',
        'Picture robo.png',
        'Address SPB, lenina 10',
        'State and City Uttar Pradesh Lucknow',
    )
    registration_page.close_submiting_form()

