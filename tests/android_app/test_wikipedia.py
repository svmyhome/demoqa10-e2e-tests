import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_skip_search_text():
    input_text = 'Appium'
    with allure.step('Welcome screen'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

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


def test_onboarding_search_text():
    with allure.step('Welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages')
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with allure.step('New ways to explore'):
        browser.element((
            AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with allure.step('Reading list with sync'):
        browser.element((
            AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with allure.step('Data & Privacy'):
        browser.element((
            AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Data & Privacy'))
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()

    with allure.step('Click to search'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_announcement_text")).should(
            have.text('Customize your Explore feed')
        )
