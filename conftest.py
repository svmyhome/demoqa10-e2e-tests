import os

import dotenv
import pytest
from selene import browser
from selenium import webdriver

import project
from utils import attach
from selenium.webdriver.chrome.options import Options

DEFAULT_BROWSER_VERSION = "121.0"


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='121.0')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    dotenv.load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    browser.config.base_url = project.config.base_url
    browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.timeout = project.config.timeout

    options = Options()
    selenoid_capabilities = {
        "browserName": project.config.driver_name,
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    # login = project.config.selenoid_login
    # password = project.config.selenoid_password
    login = os.getenv('selenoid_login')
    password = os.getenv('selenoid_password')
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options,
    # )
    driver = webdriver.Remote(
        command_executor=f"http://192.168.0.36:4444/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
