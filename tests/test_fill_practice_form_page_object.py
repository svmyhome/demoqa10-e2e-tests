from demoqa10_e2e_tests.pages.registration_page import RegistrationPage
from demoqa10_e2e_tests.test_data import users


def test_fill_practice_form_with_revision_table_hi_level(setup_browser):
    worker = users.advanced_user

    registration_page = RegistrationPage()

    registration_page.open_page()

    registration_page.register(worker)

    registration_page.should_have_registered_user_with(worker)
