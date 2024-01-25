import pytest
from selene import browser

@pytest.fixture
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1300
    browser.config.window_height = 2000