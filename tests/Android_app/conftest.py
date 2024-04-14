import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(
        {
            # Specify device and os_version for testing
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            # Set URL of the application under test
            "app": "bs://sample.app",
            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "vladimir_jrImUv",
                "accessKey": "QaxapbbXmTDusDMS1gwF",
            },
        }
    )

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
