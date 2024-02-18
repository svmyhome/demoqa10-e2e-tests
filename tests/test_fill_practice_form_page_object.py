import os

from selene import browser, be, have

from demoqa10_e2e_tests.pages.registartion_page import RegistrationPage

YEAR = '2019'
MONTH = '8'
DAY = '01'


def test_fill_practice_form_with_revision(browser_management):
    user_registration = RegistrationPage()

    user_registration.open_page()

    user_registration.fill_first_name('Ivan')
    user_registration.fill_last_name('Petrov')
    user_registration.fill_email('qaz@mail.ru')

    user_registration.gender_choose('Male')

    user_registration.fill_mobile('0123456789')

    user_registration.fill_date_of_birth(YEAR, MONTH, DAY)

    user_registration.fill_subjects('Physics')

    user_registration.hobbies_choose('Sports', 'Reading', 'Music')

    user_registration.select_picture('../README.md')

    user_registration.fill_current_address('SPB, lenina 10')

    user_registration.state_choose('Uttar Pradesh')

    user_registration.city_choose('Lucknow')

    user_registration.submit()

    user_registration.assert_fill_form(
        'Student Name Ivan Petrov',
        'Student Email qaz@mail.ru',
        'Gender Male',
        'Mobile 0123456789',
        'Date of Birth 01 September,2019',
        'Subjects Physics',
        'Hobbies Sports, Reading, Music',
        'Picture README.md',
        'Address SPB, lenina 10',
        'State and City Uttar Pradesh Lucknow',
    )


def test_fill_practice_form_with_revision_table(browser_management):
    user_registration = RegistrationPage()

    user_registration.open_page().fill_first_name('Ivan').fill_last_name(
        'Petrov'
    ).fill_email('qaz@mail.ru')

    user_registration.gender_choose('Male')

    user_registration.fill_mobile('0123456789')

    user_registration.fill_date_of_birth(YEAR, MONTH, DAY)

    user_registration.fill_subjects('Physics')

    user_registration.hobbies_choose('Sports', 'Reading', 'Music')

    user_registration.select_picture('../README.md')

    user_registration.fill_current_address('SPB, lenina 10')

    user_registration.state_choose('Uttar Pradesh').city_choose('Lucknow')

    user_registration.submit()

    user_registration.get_form_table_cells().should(
        have.exact_texts(
            ('Student Name', 'Ivan Petrov'),
            ('Student Email', 'qaz@mail.ru'),
            ('Gender', 'Male'),
            ('Mobile', '0123456789'),
            ('Date of Birth', '01 September,2019'),
            ('Subjects', 'Physics'),
            ('Hobbies', 'Sports, Reading, Music'),
            ('Picture', 'README.md'),
            ('Address', 'SPB, lenina 10'),
            ('State and City', 'Uttar Pradesh Lucknow'),
        )
    )
