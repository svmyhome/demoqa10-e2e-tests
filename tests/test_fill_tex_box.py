from selene import browser, have

from demoqa10_e2e_tests.application import app
from demoqa10_e2e_tests.data.users import SimpleUser
from demoqa10_e2e_tests.pages.text_box_registration_page import TextBoxRegistrationPage


def test_fill_text_box_left_panel(browser_management):
    simple_user = SimpleUser('Ivan', 'Ivan@mail.ru', 'SPB, Nevsky 10', 'SPB, Nevsky 10')

    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.fill(simple_user)
    app.simple_registration_page.submit()

    browser.all('#output p').should(
        have.exact_texts(
            f'Name:{simple_user.full_name}',
            f'Email:{simple_user.email}',
            f'Current Address :{simple_user.current_address}',
            f'Permananet Address :{simple_user.permanent_address}',
        )
    )
