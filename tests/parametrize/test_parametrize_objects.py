import allure
import pytest

from tests import users
from tests.users import FixtureUserWithoutRepr

user_without_fixture_1 = users.FixtureUserWithoutRepr('Iba', 1, 'kmdkmkcmd', 'qazwsx')
user_without_fixture_2 = users.FixtureUserWithoutRepr('Iba', 2, 'kmdkmkcmd', 'qazwsx')
user_with_fixture_1 = users.FixtureUserWithRepr('Iba', 1, 'kmdkmkcmd', 'qazwsx')
user_with_fixture_2 = users.FixtureUserWithRepr('Iba', 2, 'kmdkmkcmd', 'qazwsx')


def get_name_user(user: FixtureUserWithoutRepr):
    return f'{user.full_name} {user.id}'


@allure.feature('Object')
@allure.story('parametrize')
@allure.title("Parametrize with object")
@pytest.mark.parametrize("user", [user_without_fixture_1, user_without_fixture_2])
def test_parametrize_with_object(user):
    pass


@allure.feature('Object')
@allure.story('parametrize')
@allure.title("Parametrize with object from string")
@pytest.mark.parametrize(
    "user", [user_without_fixture_1, user_without_fixture_2], ids=str
)
def test_parametrize_with_object_string(user):
    pass


@allure.feature('Object')
@allure.story('parametrize')
@allure.title("Parametrize with object from method")
@pytest.mark.parametrize(
    "user", [user_without_fixture_1, user_without_fixture_2], ids=get_name_user
)
def test_parametrize_with_object_method(user):
    pass


@allure.feature('Object')
@allure.story('parametrize')
@allure.title("Parametrize with object from __repr__")
@pytest.mark.parametrize("user", [user_with_fixture_1, user_with_fixture_2], ids=repr)
def test_parametrize_with_object_method(user):
    pass
