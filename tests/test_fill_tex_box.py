import allure
from allure_commons.types import Severity

from demoqa10_e2e_tests.application import app
from demoqa10_e2e_tests.test_data import users


@allure.tag('DemoQA', 'Проверка внутри Page object')
@allure.feature('Text Box')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='Text Box Form')
def test_fill_text_box_left_panel():
    worker = users.simple_user

    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.fill(worker)
    app.profile.should_have_submitted_info(worker)
