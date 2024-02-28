import pytest
import allure
from allure_commons.types import Severity


@allure.tag('PASS', 'Проверка внутри Page object')
@allure.feature('Text Box 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='PASS')
def test_pass_1():
    with allure.step('Open page'):
        print()

    with allure.step('Submit form'):
        print()

@allure.tag('PASS', 'Проверка внутри Page object')
@allure.feature('Text Box 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='PASS')
def test_pass_2():
    with allure.step('Open page'):
        print()

    with allure.step('Submit form'):
        print()

@allure.tag('PASS', 'Проверка внутри Page object')
@allure.feature('Text Box 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='PASS')
def test_pass_3():
    with allure.step('Open page'):
        print()

    with allure.step('Submit form'):
        print()



@allure.tag('PASS', 'Проверка внутри Page object')
@allure.feature('Text Box 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='PASS')
def test_pass_4():
    with allure.step('Open page'):
        print()

    with allure.step('Submit form'):
        print()


@allure.tag('PASS', 'Проверка внутри Page object')
@allure.feature('Text Box 1')
@allure.story('Register the user')
@allure.label('OWNER', 'Vladimir')
@allure.severity(Severity.BLOCKER)
@allure.link('https://demoqa.com', name='PASS')
def test_pass_5():
    with allure.step('Open page'):
        print()

    with allure.step('Submit form'):
        print()