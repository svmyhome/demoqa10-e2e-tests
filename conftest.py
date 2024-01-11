import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_config():
    browser.config.window_width = 1000
    browser.config.window_height = 1000


@pytest.fixture(scope="function")
def open_browser_google(browser_config):
    print("Open browser")
    browser.open("https://google.com")

    yield
    browser.quit()
    print("Close browser")


@pytest.fixture(scope="function")
def open_browser_demoqa(browser_config):
    browser.open("https://demoqa.com/text-box")

    yield
    browser.quit()


@pytest.fixture
def login_page(open_browser_google):
    print("Login page opened")


@pytest.fixture
def user():
    print("User")
    return "username", "password"
