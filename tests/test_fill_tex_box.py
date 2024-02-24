from selene import browser, have

from demoqa10_e2e_tests.application import app
from demoqa10_e2e_tests.test_data import users


def test_fill_text_box_left_panel(browser_management):
    worker = users.simple_user

    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.fill(worker)
    app.simple_registration_page.submit()

    browser.all('#output p').should(
        have.exact_texts(
            f'Name:{worker.full_name}',
            f'Email:{worker.email}',
            f'Current Address :{worker.current_address}',
            f'Permananet Address :{worker.permanent_address}',
        )
    )
