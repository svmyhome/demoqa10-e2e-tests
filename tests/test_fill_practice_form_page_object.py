import allure
from allure_commons.types import Severity

from demoqa10_e2e_tests.test_data import users
from demoqa10_e2e_tests.pages.registration_page import RegistrationPage


@allure.tag('DemoQA', 'Проверка внутри Page object')
@allure.feature('Registration Form 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='Practice Form')
def test_fill_practice_form_with_revision_table_hi_level(browser_management):
    worker = users.advanced_user

    registration_page = RegistrationPage()

    registration_page.open_page()

    registration_page.register(worker)

    registration_page.should_have_registered_user_with(worker)
