# https://demoqa.com/automation-practice-form
from selene import browser, be, have
import pytest


# def test_fill_practice_form():
#     browser.open('https://demoqa.com/automation-practice-form')
#
#     browser.element('#firstName').should(be.blank).type('Ivan')
#     browser.element('#lastName').should(be.blank).type('Petrov')
#     browser.element('#userEmail').should(be.blank).type('qaz@mail.ru')
#     # browser.element('#genterWrapper [name=gender]').should(have.exact_text('Male')).click()
#     # browser.element('#genterWrapper [name=gender]').all(have.exact_text('Male')).click()
#     browser.element('#userNumber').should(be.blank).type('123456789')
#     # browser.element('#userNumber').should(be.blank).type('123456789')
#     # browser.element('#userNumber').should(be.blank).type('123456789')
#     browser.element('#currentAddress').should(be.blank).type('1234 casc csdc 56789')

def test_firt():
    browser.open('https://dzen.ru/?yredirect=true')