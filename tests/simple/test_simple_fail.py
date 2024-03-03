import allure
import pytest
from allure_commons.types import Severity


@allure.tag('Simple Fail')
@allure.feature('Simple')
@allure.story('Fail')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Fail Simple test 1")
def test_simple_fail_1():
    assert False


@allure.tag('Simple Fail')
@allure.feature('Simple')
@allure.story('Fail')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Fail Simple test 2")
def test_simple_fail_2():
    assert False


@allure.tag('Simple Fail')
@allure.feature('Simple')
@allure.story('Fail')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Fail Simple test 3")
def test_simple_fail_3():
    assert False
