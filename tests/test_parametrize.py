"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import have, browser


@pytest.mark.parametrize("manage_desktop_browser", [(1600, 1000)], indirect=True)
def test_github_desktop(manage_desktop_browser):
    browser.open('/')

    browser.element('.header-menu-wrapper').element('a[href="/login"]').click()

    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("manage_mobile_browser", [(390, 844)], indirect=True)
def test_github_mobile(manage_mobile_browser):
    browser.open('/')

    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
