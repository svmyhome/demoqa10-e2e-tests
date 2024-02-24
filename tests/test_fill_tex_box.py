import allure
from allure_commons.types import Severity
from selene import browser, have

from demoqa10_e2e_tests.application import app
from demoqa10_e2e_tests.test_data import users



@allure.tag('DemoQA')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'QAauto')
@allure.feature('Simple registration form')
@allure.story('Sent simple registration form')
@allure.link('https://demoqa.com', name='Text Box')
def test_fill_text_box_left_panel(browser_management):
    worker = users.simple_user

    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.fill(worker)
    app.profile.should_have_submited_info(worker)
