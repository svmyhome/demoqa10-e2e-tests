import os

from selene import browser, be, have


def test_fill_practice_form(browser_management):
    year = '2019'
    month = '7'
    day = '01'
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('qaz@mail.ru')

    browser.element('[for=gender-radio-1]').click()

    browser.element('#userNumber').should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(f"[value='{year}']").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(f"[value='{month}']").click()
    browser.element(f".react-datepicker__day--0{day}[tabindex='-1']").click()

    browser.element("#subjectsContainer").click().element('#subjectsInput').type('p')

    browser.element("#react-select-2-option-0").click()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('README.md'))

    browser.element('#currentAddress').should(be.blank).type('1234 casc csdc 56789')

    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.all('.table-responsive tbody>tr').should(
        have.exact_texts(
            'Student Name Ivan Petrov',
            'Student Email qaz@mail.ru',
            'Gender Male',
            'Mobile 0123456789',
            'Date of Birth 01 August,2019',
            'Subjects Physics',
            'Hobbies Sports, Reading, Music',
            'Picture README.md',
            'Address 1234 casc csdc 56789',
            'State and City Haryana Karnal',
        )
    )
