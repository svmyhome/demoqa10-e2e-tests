import dotenv
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    dotenv.load_dotenv()
    user_name = os.getenv('userName')
    access_key = os.getenv('accessKey')
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": "bs://sample.app",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": user_name,
                "accessKey": access_key,
            },
        }
    )

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
