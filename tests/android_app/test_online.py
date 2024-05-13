import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_text():
    with allure.step('Welcome screen'):
        browser.element(
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).click()

    with allure.step('Click to search'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Магазины"]')).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.XPATH,
                         "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[3]")).click()

    with allure.step('Assert text found'):
        browser.all((AppiumBy.XPATH,
                     '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]')).click()

    with allure.step('Assert text found'):
        browser.all(
            (AppiumBy.XPATH,
             '//android.widget.TextView[@resource-id="TitleCenter" and @text="Санкт-Петербург, Магнитогорская ул., 11, лит. Н"]')
        ).click()


def test_search_lenta_real():
    with allure.step('Add address'):
        browser.element((AppiumBy.ID, "com.icemobile.lenta.prod:id/onboardingAddAddress")).click()

    with allure.step('Allow access'):
        browser.element(
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).click()

    with allure.step('Continue'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="BottomButton"]')).click()


    #//android.widget.Button[@resource-id="android:id/ok"]
    with allure.step('Click to search'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.ImageButton[@resource-id="com.icemobile.lenta.prod:id/storiesClose"]')).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="com.icemobile.lenta.prod:id/textName" and @text="Груши Вильямс, весовые"]')).click()

    with allure.step('Assert text found'):
        browser.all((AppiumBy.XPATH,
                     '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.icemobile.lenta.prod:id/catalogEcommScreenList"]/android.widget.LinearLayout[1]/android.widget.LinearLayout')).should(
            have.text("Груши Вильямс, весовые"))


def test_search_lenta_emulator():
    with allure.step('Add address'):
        browser.element((AppiumBy.ID, "com.icemobile.lenta.prod:id/onboardingAddAddress")).should(be.clickable)
        browser.element((AppiumBy.ID, "com.icemobile.lenta.prod:id/onboardingAddAddress")).click()

    with allure.step('Allow access'):
        browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).should(be.clickable)
        browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).click()

    with allure.step('Continue'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="BottomButton"]')).should(be.clickable)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="BottomButton"]')).click()

    with allure.step('Click to search'):
        browser.element((AppiumBy.XPATH,'//android.widget.ImageButton[@resource-id="com.icemobile.lenta.prod:id/storiesClose"]')).should(be.clickable)
        browser.element((AppiumBy.XPATH,'//android.widget.ImageButton[@resource-id="com.icemobile.lenta.prod:id/storiesClose"]')).click()

    with allure.step('Type the text'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.icemobile.lenta.prod:id/textName" and @text="Груши Вильямс, весовые"]')).should(be.clickable)
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.icemobile.lenta.prod:id/textName" and @text="Груши Вильямс, весовые"]')).click()

    with allure.step('Assert text found'):
        browser.all((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.icemobile.lenta.prod:id/catalogEcommScreenList"]/android.widget.LinearLayout[1]/android.widget.LinearLayout')).should(be.visible)
        browser.all((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.icemobile.lenta.prod:id/catalogEcommScreenList"]/android.widget.LinearLayout[1]/android.widget.LinearLayout')).should(
            have.text("Груши Вильямс, весовые"))