import dotenv
import pytest
from selene import browser
from selenium import webdriver

import project
from utils import attach
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser(request):
    dotenv.load_dotenv()
    browser.config.base_url = project.config.base_url
    browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.timeout = project.config.timeout

    options = Options()
    selenoid_capabilities = {
        "browserName": project.config.driver_name,
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
