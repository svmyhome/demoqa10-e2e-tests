import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_settings():
    browser.config.base_url = "https://github.com/"


@pytest.fixture(
    scope='function',
    params=[(1920, 1000), (1600, 1000), (1366, 1000), (1084, 1000)],
    ids=str,
)
def manage_desktop_browser(request, browser_settings):
    browser.config.window_width, browser.config.window_height = request.param

    yield
    browser.quit()


@pytest.fixture(
    scope='function', params=[(375, 667), (390, 844), (430, 932), (1024, 1366)], ids=str
)
def manage_mobile_browser(request, browser_settings):
    browser.config.window_width, browser.config.window_height = request.param

    yield
    browser.quit()


@pytest.fixture(
    scope='function',
    params=[
        (1920, 1000),
        (1600, 1000),
        (1366, 1000),
        (1084, 1000),
        (375, 667),
        (390, 844),
        (430, 932),
    ],
    ids=str,
)
def manage_desktop_mobile_browser(request, browser_settings):
    browser.config.window_width, browser.config.window_height = request.param

    yield
    browser.quit()
