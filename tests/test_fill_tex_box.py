from selene import browser, have

from demoqa10_e2e_tests.application import app
from demoqa10_e2e_tests.data.users import SimpleUser
from demoqa10_e2e_tests.pages.text_box_registration_page import TextBoxRegistrationPage


def test_fill_text_box(browser_management):
    simple_user = SimpleUser('Ivan', 'Ivan@mail.ru', 'SPB, Nevsky 10', 'SPB, Nevsky 10')

    registration_page = TextBoxRegistrationPage()
    registration_page.open()
    registration_page.fill_fullname(simple_user.full_name).fill_email(
        simple_user.email
    ).fill_current_address(simple_user.current_address).fill_permanent_address(
        simple_user.permanent_address
    ).submit()

    browser.all('#output p').should(
        have.exact_texts(
            'Name:Ivan',
            'Email:Ivan@mail.ru',
            'Current Address :SPB, Nevsky 10',
            'Permananet Address :SPB, Nevsky 10',
        )
    )


def test_fill_text_box_app(browser_management):
    simple_user = SimpleUser('Ivan', 'Ivan@mail.ru', 'SPB, Nevsky 10', 'SPB, Nevsky 10')

    app.simple_registration_page.open()
    app.simple_registration_page.fill(simple_user)
    app.simple_registration_page.submit()  # TODO

    browser.all('#output p').should(
        have.exact_texts(
            'Name:Ivan',
            'Email:Ivan@mail.ru',
            'Current Address :SPB, Nevsky 10',
            'Permananet Address :SPB, Nevsky 10',
        )
    )


def test_fill_text_box_panel(browser_management):
    simple_user = SimpleUser('Ivan', 'Ivan@mail.ru', 'SPB, Nevsky 10', 'SPB, Nevsky 10')

    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.fill(simple_user)
    app.simple_registration_page.submit()

    browser.all('#output p').should(
        have.exact_texts(
            'Name:Ivan',
            'Email:Ivan@mail.ru',
            'Current Address :SPB, Nevsky 10',
            'Permananet Address :SPB, Nevsky 10',
        )
    )
