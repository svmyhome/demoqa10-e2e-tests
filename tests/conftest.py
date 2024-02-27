import allure
import pytest
from selene import browser
import project
import dotenv


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    dotenv.load_dotenv()
    with allure.step('Driver configuration'):
        browser.config.base_url = project.config.base_url
        browser.config.driver_name = project.config.driver_name
        browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
        browser.config.window_width = project.config.window_width
        browser.config.window_height = project.config.window_height
        browser.config.timeout = project.config.timeout

    yield
    with allure.step('Close driver'):
        browser.quit()
