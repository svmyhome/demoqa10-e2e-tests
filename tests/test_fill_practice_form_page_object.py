from demoqa10_e2e_tests.test_data import users
from demoqa10_e2e_tests.pages.registartion_page import RegistrationPage


def test_fill_practice_form_with_revision_table_hi_level(browser_management):
    worker = users.advanced_user

    registration_page = RegistrationPage()

    registration_page.open_page()

    registration_page.register(worker)

    registration_page.should_have_registered_user_with(worker)
