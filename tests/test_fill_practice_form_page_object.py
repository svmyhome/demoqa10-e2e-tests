from demoqa10_e2e_tests.data.users import User
from demoqa10_e2e_tests.pages.registartion_page import RegistrationPage
from demoqa10_e2e_tests.resource import Hobbies


def test_fill_practice_form_with_revision_table_hi_level(browser_management):
    worker = User(
        first_name='Ivan',
        last_name='Petrov',
        email='qaz@mail.ru',
        gender='Male',
        mobile='0123456789',
        date_of_birth_year='1980',
        date_of_birth_month='January',
        date_of_birth_day='10',
        subjects='Physics',
        hobbies=[Hobbies.sport.value, Hobbies.reading.value, Hobbies.music.value],
        picture='robo.png',
        current_address='SPB, lenina 10',
        state='Uttar Pradesh',
        city='Lucknow',
    )

    registration_page = RegistrationPage()

    registration_page.open_page()

    registration_page.register(worker)

    registration_page.should_have_registered_user_with(worker)