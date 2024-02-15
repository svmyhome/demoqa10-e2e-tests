import os

from selene import browser, be, have, command

YEAR = '2019'
MONTH = '7'
DAY = '01'


def test_fill_practice_form_without_revision(browser_management):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('qaz@mail.ru')

    browser.element('[for=gender-radio-1]').click()

    browser.element('#userNumber').should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(f"[value='{YEAR}']").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(f"[value='{MONTH}']").click()
    browser.element(f".react-datepicker__day--0{DAY}[tabindex='-1']").click()

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


def test_fill_practice_form_with_revision_1(browser_management):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('qaz@mail.ru')

    browser.all('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    # browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    # browser.element('[name=gender][value=Male]+label').click()
    # browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::*').click()

    browser.element('#userNumber').should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").type('2012')
    # browser.element(".react-datepicker__year-select").click()
    # browser.element("[value='2019']").click()
    browser.element(".react-datepicker__month-select").click()
    # browser.element('[class~="react-datepicker__month-select"]').click()
    # browser.element("[value='7']").click()
    browser.element('[class~="react-datepicker__month-select"]').all('option')[
        4
    ].click()
    browser.element(f".react-datepicker__day--001[tabindex='-1']").click()

    browser.element("#subjectsContainer").click().element('#subjectsInput').type('p')

    browser.element("#react-select-2-option-0").click()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('README.md'))

    browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element('#currentAddress').perform(
        command.js.set_value('1234 casc 33e csdc 56789')
    )
    # browser.element('#currentAddress').should(be.blank).type('1234 casc csdc 56789')

    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    # browser.all('.table tbody>tr').should(
    #     have.exact_texts(
    #         'Student Name Ivan Petrov',
    #         'Student Email qaz@mail.ru',
    #         'Gender Male',
    #         'Mobile 0123456789',
    #         'Date of Birth 01 August,2019',
    #         'Subjects Physics',
    #         'Hobbies Sports, Reading, Music',
    #         'Picture README.md',
    #         'Address 1234 casc csdc 56789',
    #         'State and City Haryana Karnal',
    #     )
    # )
    list_data = [
        'Student Name',
        'Ivan Petrov',
        'Student Email',
        'qaz@mail.ru',
        'Gender',
        'Male',
        'Mobile',
        '0123456789',
        'Date of Birth',
        '01 August,2019',
        'Subjects',
        'Physics',
        'Hobbies',
        'Sports, Reading, Music',
        'Picture',
        'README.md',
        'Address',
        '1234 casc csdc 56789',
        'State and City',
        'Haryana Karnal',
    ]
    browser.element('.table').all('td').should(have.texts())