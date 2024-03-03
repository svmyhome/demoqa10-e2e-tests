import allure
import pytest
from allure_commons.types import Severity


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


@pytest.mark.skip('Тесты пропущены специально')
@allure.tag('Simple Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Skipped Simple test 2")
def test_simple_skip_2():
    pass


@pytest.mark.skip('Тесты пропущены специально')
@allure.tag('Simple Skipped')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Skipped Simple test 3")
def test_simple_skip_3():
    pass
