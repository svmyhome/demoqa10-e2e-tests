import os

import allure
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    with allure.step('Driver configuration'):
        browser.config.base_url = os.getenv('base_url', 'https://demoqa.com')
        browser.config.driver_name = os.getenv('driver_name', 'chrome')
        browser.config.hold_driver_at_exit = (
            os.getenv('hold_driver_at_exit', 'false').lower() == 'true'
        )
        browser.config.window_width = os.getenv('window_width', 1300)
        browser.config.window_height = os.getenv('window_height', 2000)
        browser.config.timeout = float(os.getenv('timeout', '4.0'))

    yield
    with allure.step('Close driver'):
        browser.quit()
