from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class Onbording:

    def should_have_text(self, value):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text(value)
        )

    def click_onboarding_forward_button(self):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    def click_onboarding_done_button(self):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()

    def should_have_success_onbording(self, value):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')
        ).should(have.text(value))


onbording = Onbording()
