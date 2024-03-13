import allure
import pytest
from allure_commons.types import Severity


@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def my_browser(request):
    if request.param == "Chrome":
        return "Chrome"
    if request.param == "Firefox":
        return "Firefox"
    if request.param == "Safari":
        return "Safari"


@allure.feature('Fixture')
@allure.story('Parametrize')
@allure.title("Parametrize Fixture")
def test_parametrize_fixture(my_browser):
    print(my_browser)


@allure.feature('Fixture')
@allure.story('Indirect')
@allure.title("Parametrize Fixture indirect only Chrome and Firefox")
@pytest.mark.parametrize("my_browser", ["Chrome", "Firefox"], indirect=True)
def test_parametrize_fixture_with_indirect_1(my_browser):
    print(my_browser)


@allure.feature('Fixture')
@allure.story('Indirect')
@allure.title("Parametrize Fixture indirect only Chrome")
@pytest.mark.parametrize("my_browser", ["Chrome"], indirect=True)
def test_parametrize_fixture_with_indirect_2(my_browser):
    print(my_browser)


chrome_only = pytest.mark.parametrize("my_browser", ["Chrome"], indirect=True)

@allure.feature('Fixture')
@allure.story('Indirect')
@allure.title("Parametrize Fixture indirect only Chrome")
@chrome_only
def test_parametrize_fixture_with_indirect_3(my_browser):
    print(my_browser)