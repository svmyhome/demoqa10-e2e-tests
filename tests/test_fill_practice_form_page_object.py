import datetime
from demoqa10_e2e_tests.data.users import User

from selene import have

from demoqa10_e2e_tests.pages.registartion_page import RegistrationPage, Hobbies

YEAR = 2019
MONTH = 8
DAY = 1


def test_fill_practice_form_with_revision_table_hi_level(browser_management):
    user = User(
        'Ivan',
        'Petrov',
        'qaz@mail.ru',
        'Male',
        '0123456789',
        datetime.date(YEAR, MONTH, DAY),
        ('p', 'Physics'),
        [Hobbies.sport, Hobbies.reading, Hobbies.music],
        'README.md',
        'SPB, lenina 10',
        'Uttar Pradesh',
        'Lucknow',
    )
    full_registration_page = RegistrationPage()

    full_registration_page.open_page()

    full_registration_page.register(user)

    full_registration_page.submit()

    full_registration_page.get_form_table_cells().should(
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
