"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


def test_github_desktop(manage_desktop_mobile_browser):
    if browser.config.window_width <= 375 or browser.config.window_height <= 932:
        pytest.skip("This is mobile resolution")
    else:
        browser.open('/')

        browser.element('.header-menu-wrapper').element('a[href="/login"]').click()

        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(manage_desktop_mobile_browser):
    if browser.config.window_width <= 375 or browser.config.window_height <= 932:
        browser.open('/')

        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link.HeaderMenu-link--sign-in').click()

        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))

    else:
        pytest.skip("This is mobile desktop")
