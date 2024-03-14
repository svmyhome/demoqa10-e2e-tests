"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser, have


def test_github_desktop(manage_desktop_browser):
    browser.open('/')

    browser.element('.header-menu-wrapper').element('a[href="/login"]').click()

    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(manage_mobile_browser):
    browser.open('/')

    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))




