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
from demoqa10_e2e_tests.utils.resource import relative_from_root


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    if project.settings.platform_name == 'android':
        options = UiAutomator2Options()

        options.set_capability("platformName", project.settings.platform_name)
        if not config.runs_on_bstack:
            options.set_capability('udid', project.settings.udid)
        if project.settings.android_device_name:
            options.set_capability("deviceName", project.settings.android_device_name)

        if project.settings.android_platform_version:
            options.set_capability(
                "platformVersion",
                project.settings.android_platform_version,
            )

        if project.settings.appWaitActivity:
            options.set_capability("appWaitActivity", project.settings.appWaitActivity)

        options.set_capability(
            "app",
            (
                project.settings.app_path
                if (project.settings.app_path.startswith('/') or config.runs_on_bstack)
                else relative_from_root(project.settings.app_path)
            ),
        )

        if config.runs_on_bstack:

            options.set_capability(
                'bstack:options',
                {
                    "projectName": project.settings.android_project_name,
                    "buildName": "browserstack-build-remote",
                    "sessionName": "Android tests Remote",
                    "userName": config.user_name,
                    "accessKey": config.access_key,
                },
            )

    with allure.step("Init app session"):
        browser.config.driver = webdriver.Remote(
            project.settings.base_url, options=options
        )
    browser.config.timeout = project.settings.time_out
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach_png()

    attach_page_source()

    session_id = browser.driver.session_id

    with allure.step(f"Tear down session {session_id}"):
        browser.quit()
    if config.runs_on_bstack:
        attach_video(session_id)
