import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_text():
    input_text = 'Appium'
    with allure.step('Welcome screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with allure.step('Click to search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            input_text
        )
    with allure.step('Assert text found'):
        results = browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text(input_text))