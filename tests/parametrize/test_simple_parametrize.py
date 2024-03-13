import allure
import pytest
from allure_commons.types import Severity

from demoqa10_e2e_tests.test_data import users
from demoqa10_e2e_tests.test_data.users import SimpleUser

# pytestmark = pytest.mark.skip(reason="Когда нужно пропустить весь файл")

is_linux = True
is_windows = False
user_1 = users.simple_user


@allure.tag('Simple parametrize')
@allure.feature('Simple')
@allure.story('parametrize')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Parametrize')
@allure.title("Simple parametrize")
@pytest.mark.parametrize("os", ["linux", "windows"])
def test_simple_parametrize_1(os):
    print(os)


@allure.feature('Simple')
@allure.story('parametrize')
@allure.title("Simple parametrize")
@pytest.mark.parametrize("os, browser_1", [("linux", "Chrome"), ("windows", "Firefox")])
def test_simple_parametrize_2(os, browser_1):
    print(os, browser_1)


@allure.tag('Simple parametrize multiply by everything')
@allure.feature('Simple')
@allure.story('parametrize')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Parametrize')
@allure.title("Simple parametrize multiply by everything")
@pytest.mark.parametrize("os", ["linux", "windows"])
@pytest.mark.parametrize("browser_1", ["Chrome", "Firefox"])
def test_simple_parametrize_3(os, browser_1):
    print(os, browser_1)


@allure.tag('Simple parametrize with ids by str USER')
@allure.feature('Simple')
@allure.story('parametrize')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Parametrize')
@allure.title("Simple parametrize with ids by str USER")
@pytest.mark.parametrize("user", [user_1], ids=str)
def test_simple_parametrize_4(user):
    print(user)


@allure.tag('Simple parametrize multiply by everything and XFAIL for one')
@allure.feature('Simple')
@allure.story('parametrize')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Parametrize')
@allure.title("Simple parametrize multiply by everything and XFAIL for one")
@pytest.mark.parametrize(
    "browser_1",
    [
        pytest.param("Chrome", id="My Chrome"),
        pytest.param("Firefox", marks=[pytest.mark.slow]),
        pytest.param("Opera", marks=[pytest.mark.xfail(reason="Task 1234")]),
    ],
)
def test_simple_parametrize_5(browser_1):
    print(browser_1)
