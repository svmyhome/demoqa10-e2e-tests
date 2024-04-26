from typing import Literal

import allure
import allure_commons
import dotenv
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
import os
import requests
import config
import project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    # dotenv.load_dotenv()
    # user_name = os.getenv('userName')
    # access_key = os.getenv('accessKey')
    if project.config.platform_name == 'android':
        options = UiAutomator2Options().load_capabilities(
            {
                "platformName": project.config.platform_name,
                "platformVersion": project.config.platform_version,
                "deviceName": "Google Pixel 3",
                "app": project.config.app_path,
                'bstack:options': {
                    "projectName": project.config.android_project_name,
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": config.user_name,
                    "accessKey": config.access_key,
                },
            }
        )
    elif project.config.platform_name == 'ios':
        options = XCUITestOptions().load_capabilities(
            {
                "app": "bs://sample.app",
                "deviceName": "iPhone 11 Pro",
                "platformName": "ios",
                "platformVersion": "13",
                "bstack:options": {
                    "userName": config.user_name,
                    "accessKey": config.access_key,
                    "projectName": project.config.ios_project_name,
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                },
            }
        )
    with allure.step("Init app session"):
        browser.config.driver = webdriver.Remote(
            "http://hub.browserstack.com/wd/hub", options=options
        )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='XML page',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step("Tear down session"):
        browser.quit()

    attach_video(session_id)


def attach_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.user_name, config.access_key),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
