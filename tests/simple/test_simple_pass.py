import allure
from allure_commons.types import Severity


@allure.tag('Simple Pass')
@allure.feature('Simple')
@allure.story('Pass')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Simple test 1")
def test_simple_pass_1():
    pass


@allure.tag('Simple Pass')
@allure.feature('Simple')
@allure.story('Skip')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Simple test 2")
def test_simple_pass_2():
    pass


@allure.tag('Simple Pass')
@allure.feature('Simple')
@allure.story('Skip')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Simple test 3")
def test_simple_pass_3():
    pass


@allure.tag('Simple Pass')
@allure.feature('Simple')
@allure.story('Skip')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com/automation-practice-form', name='Pass')
@allure.title("Simple test 4")
def test_simple_pass_4():
    pass
