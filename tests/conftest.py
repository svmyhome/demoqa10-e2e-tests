import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
import config
import project
from demoqa10_e2e_tests.utils.allure_attach import (
    attach_png,
    attach_page_source,
    attach_video,
)


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    if project.settings.platform_name == 'android':
        options = UiAutomator2Options().load_capabilities(
            {
                "platformName": project.settings.platform_name,
                "platformVersion": project.settings.platform_version,
                "deviceName": "Google Pixel 3",
                "app": project.settings.app_path,
                'bstack:options': {
                    "projectName": project.settings.android_project_name,
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": config.user_name,
                    "accessKey": config.access_key,
                },
            }
        )
    elif project.settings.platform_name == 'ios':
        options = XCUITestOptions().load_capabilities(
            {
                "app": "bs://sample.app",
                "deviceName": "iPhone 11 Pro",
                "platformName": "ios",
                "platformVersion": "13",
                "bstack:options": {
                    "userName": config.user_name,
                    "accessKey": config.access_key,
                    "projectName": project.settings.ios_project_name,
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                },
            }
        )
    with allure.step("Init app session"):
        browser.config.driver = webdriver.Remote(
            "http://hub.browserstack.com/wd/hub", options=options
        )
    browser.config.timeout = project.settings.time_out
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach_png()

    attach_page_source()

    session_id = browser.driver.session_id

    with allure.step("Tear down session"):
        browser.quit()

    attach_video(session_id)
