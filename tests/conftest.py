import allure
import pytest
from selene import browser


@pytest.fixture
def browser_management():
    with allure.step('Driver configuration'):
        browser.config.base_url = 'https://demoqa.com'
        browser.config.window_width = 1300
        browser.config.window_height = 2000

    yield
    with allure.step('Close driver'):
        browser.quit()
