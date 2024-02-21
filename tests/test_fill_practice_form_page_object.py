import datetime
from demoqa10_e2e_tests.data.user import User

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
        'robo.png',
        'SPB, lenina 10',
        'Uttar Pradesh',
        'Lucknow',
    )
    user_registration = RegistrationPage()

    user_registration.open_page()

    user_registration.register(user)

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
            ('Picture', 'robo.png'),
            ('Address', 'SPB, lenina 10'),
            ('State and City', 'Uttar Pradesh Lucknow'),
        )
    )
