import allure
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    with allure.step('Driver configuration'):
        print()

    yield
    with allure.step('Close driver'):
        print()
