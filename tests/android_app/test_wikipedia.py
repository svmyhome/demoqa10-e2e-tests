import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from demoqa10_e2e_tests.models.onbording import onbording


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
        onbording.should_have_text('The Free Encyclopedia\n…in over 300 languages')
        onbording.click_onboarding_forward_button()

    with allure.step('New ways to explore'):
        onbording.should_have_text('New ways to explore')
        onbording.click_onboarding_forward_button()

    with allure.step('Reading list with sync'):
        onbording.should_have_text('Reading lists with sync')
        onbording.click_onboarding_forward_button()

    with allure.step('Data & Privacy'):
        onbording.should_have_text('Data & Privacy')
        onbording.click_onboarding_done_button()

    with allure.step('Click to search'):
        onbording.should_have_success_onbording('Customize your Explore feed')

