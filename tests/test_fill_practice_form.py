import allure
from selene import be, have, browser, command

from demoqa10_e2e_tests.utils.resource import relative_from_root


@allure.title("Successful fill form")
def test_fill_practice_form_with_revision(setup_browser):
    with allure.step("Open registrations form"):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    with allure.step("Consent form"):
        browser.element('.fc-cta-consent').should(be.clickable).click()

    with allure.step("Fill form"):
        browser.element('#firstName').should(be.blank).type('Ivan')
        browser.element('#lastName').should(be.blank).type('Petrov')
        browser.element('#userEmail').should(be.blank).type('qaz@mail.ru')

        browser.all('[for^=gender-radio]').element_by(have.exact_text('Male')).click()

        browser.element('#userNumber').should(be.blank).type('0123456789')

        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{2019}']").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{8}']").click()
        browser.element(
            f".react-datepicker__day--0{'01'}:not(.react-datepicker__day--outside-month)"
        ).click()

        browser.element("#subjectsContainer").click().element('#subjectsInput').type(
            'p'
        )

        browser.all("[id^=react-select-2-option]").element_by(
            have.exact_text('Physics')
        ).click()

        browser.all("[for^='hobbies-checkbox']").element_by(
            have.exact_text('Sports')
        ).click()
        browser.all("[for^='hobbies-checkbox']").element_by(
            have.exact_text('Reading')
        ).click()
        browser.all("[for^='hobbies-checkbox']").element_by(
            have.exact_text('Music')
        ).click()

        browser.element('#uploadPicture').send_keys(
            relative_from_root('resources/robo.png')
        )

        browser.element('#currentAddress').should(be.blank).type('1234 casc csdc 56789')

        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all("[id^='react-select-3-option']").element_by(
            have.exact_text('Uttar Pradesh')
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select-4-option]').element_by(
            have.exact_text('Lucknow')
        ).click()
        browser.element('#submit').click()
    with allure.step("Check form results"):
        browser.element('.table-responsive').all('tbody>tr').should(
            have.exact_texts(
                'Student Name Ivan Petrov',
                'Student Email qaz@mail.ru',
                'Gender Male',
                'Mobile 0123456789',
                'Date of Birth 01 September,2019',
                'Subjects Physics',
                'Hobbies Sports, Reading, Music',
                'Picture robo.png',
                'Address 1234 casc csdc 56789',
                'State and City Uttar Pradesh Lucknow',
            )
        )
