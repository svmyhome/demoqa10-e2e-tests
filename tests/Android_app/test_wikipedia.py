import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_search():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()


    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "Appium"
    )
    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
