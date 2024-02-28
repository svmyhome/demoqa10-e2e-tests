import allure
import pytest
from allure_commons._allure import attach
from selene import browser
import project
import dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "100.0",
    #     "selenoid:options": {"enableVNC": True, "enableVideo": True},
    # }
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
    #     options=options,
    # )
    #
    # browser = Browser(Config(driver))
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


# @pytest.fixture(scope='function')
# def setup_browser(request):
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "100.0",
#         "selenoid:options": {"enableVNC": True, "enableVideo": True},
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options,
#     )
#
#     browser = Browser(Config(driver))
#     yield browser
#
#     # attach.add_screenshot(browser)
#     # attach.add_logs(browser)
#     # attach.add_html(browser)
#     # attach.add_video(browser)
#
#     browser.quit()
