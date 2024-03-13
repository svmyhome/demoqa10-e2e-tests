import allure
import pytest
from allure_commons.types import Severity

# pytestmark = pytest.mark.skip(reason="Когда нужно пропустить весь файл")

is_linux = True
is_windows = False


@pytest.mark.skip('Тесты пропущены специально')
@allure.tag('Simple Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Skipped Simple test 1")
def test_simple_skip_1():
    pass


@pytest.mark.skip(reason='Тесты пропущены специально')
@allure.tag('Simple Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Skipped Simple test 2")
def test_simple_skip_2():
    pass


@pytest.mark.skipif(is_linux, reason='Тест пропущен так как условие is_skip = True')
@allure.tag('Simple Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("If is_linux is TRUE that test is skip")
def test_simple_skipif_1():
    pass


@pytest.mark.skipif(
    is_windows, reason='Тест не пропущен так как условие is_windows = False'
)
@allure.tag('Simple Not Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Test did not skipped because is_windows = False")
def test_simple_skipif_2():
    pass


@pytest.mark.xfail(reason='Тест упал и выводит XFAIL')
@allure.tag('Simple XFAIL')
@allure.feature('XFAIL')
@allure.story('xfail')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("TASK-1234 Test is xfail because is flaky")
def test_simple_xfail_1():
    assert 2 == 2
    assert 1 == 2
    assert 3 == 3


@allure.tag('Simple XFAIL')
@allure.feature('XPASS')
@allure.story('xpass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("TASK-1234Test is xfail because is flaky")
def test_simple_xfail_2():
    assert 2 == 2
    try:
        assert 2 == 2
    except AssertionError:
        pytest.xfail("TASK-1234 Test is xfail because is flaky")
    assert 3 == 3
