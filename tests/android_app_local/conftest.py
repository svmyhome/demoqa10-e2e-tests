import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "udid": "DUM0220121000925",
            "appWaitActivity": "org.wikipedia.*",
            "app": "/home/vladimir/Downloads/app-alpha-universal-release.apk",
        }
    )

    browser.config.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
