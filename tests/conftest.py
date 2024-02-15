import pytest
from selene import browser


@pytest.fixture()
def browser_management():
    browser.config.window_width = 1200
    browser.open('https://github.com/')