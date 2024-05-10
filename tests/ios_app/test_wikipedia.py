import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_text_ios():

    with allure.step('Click to search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("Appium")

    with allure.step('Assert text found'):
        results = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
        results.should(have.text("Appium"))


def test_open_article_ios():

    with allure.step('Click to search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("Java")

    with allure.step('Assert text found'):
        results = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
        results.should(have.text("Java"))

    with allure.step('Click to article'):
        results.should(have.text("Java")).click()
