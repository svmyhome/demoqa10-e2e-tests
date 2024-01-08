import time

from selene import browser, be, have


def test_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_fill_text_box():
    browser.open('https://demoqa.com/text-box')

    browser.element('#userName-wrapper #userName').should(be.blank).type('Petr').press_enter()
    browser.element('#userEmail-wrapper #userEmail').should(be.blank).type('Petr@mail.ru').press_enter()
    browser.element('#currentAddress-wrapper #currentAddress').should(be.blank).type('SPB')
    browser.element('#permanentAddress-wrapper #permanentAddress').should(be.blank).type('SPB')
    browser.element('#submit').should(be.clickable).click()
