import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_appium():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "Appium"
    )
    with allure.step('Verify content found'):
        results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_python():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "Python"
    )
    with allure.step('Verify content found'):
        results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))

def test_search_1234567890():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "1234567890"
    )
    with allure.step('Verify content found'):
        results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text('1234567890'))


def test_nothing_found_1():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "1234567890qaz"
    )

    with allure.step('Verify content not found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/results_text"))
        results.should(have.size(0))

def test_nothing_found_2():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "1234567890qaz"
    )

    with allure.step('Verify content not found'):
        results = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/results_text"))
        results.should(have.size(0))

def test_nothing_found_3():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "1234567890qaz"
    )

    with allure.step('Verify content not found'):
        results = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/results_text"))
        results.should(have.text('No results'))