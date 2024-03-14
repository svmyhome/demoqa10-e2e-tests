# import pytest
# from selene import browser
#
#
# @pytest.fixture(scope='function')
# def open_browser():
#     browser.open("https://github.com/")
#
#     yield
#     browser.quit()
#     print("Close browser")
#
import pytest
from selene import browser


@pytest.fixture(
    scope='function',
    params=[(1920, 1000), (1600, 1000), (1366, 1000), (1084, 1000)],
    ids=str,
)
def manage_desktop_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    browser.open("https://github.com/")

    yield
    browser.quit()
    print("Close browser")


@pytest.fixture(
    scope='function', params=[(375, 667), (390, 844), (430, 932), (1024, 1366)], ids=str
)
def manage_mobile_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    browser.open("https://github.com/")

    yield
    browser.quit()
