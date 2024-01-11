from selene import browser, be, have


def test_find_selene(open_browser_google):

    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_words_not_found_(open_browser_google):

    browser.element('[name="q"]').should(be.blank).type('12345!@#$%^&(оысриьлслыламитьм').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))

def test_fill_text_box(open_browser_demoqa):

    browser.element('#userName-wrapper #userName').should(be.blank).type('Petr').press_enter()
    browser.element('#userEmail-wrapper #userEmail').should(be.blank).type('Petr@mail.ru').press_enter()
    browser.element('#currentAddress-wrapper #currentAddress').should(be.blank).type('SPB')
    browser.element('#permanentAddress-wrapper #permanentAddress').should(be.blank).type('SPB')
    browser.element('#submit').should(be.clickable).click()
