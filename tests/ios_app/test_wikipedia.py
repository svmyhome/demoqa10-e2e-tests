import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_text():

    with allure.step('Click to search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("Appium")

    with allure.step('Assert text found'):
        results = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
        results.should(have.text("Appium"))
