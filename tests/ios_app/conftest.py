import dotenv
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    dotenv.load_dotenv()
    user_name = os.getenv('userName')
    access_key = os.getenv('accessKey')
    options = XCUITestOptions().load_capabilities(
        {
            # Set URL of the application under test
            "app": "bs://sample.app",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformName": "ios",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": user_name,
                "accessKey": access_key,
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
            },
        }
    )

    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub", options=options
    )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
