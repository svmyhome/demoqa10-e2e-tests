from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_ios():

    text_button = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
    text_button.click()

    text_input = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    text_input.type("Appium")

    text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    text_output.should(have.text("Appium"))
