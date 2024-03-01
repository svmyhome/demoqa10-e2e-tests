from selene import command, browser


def scroll_to_element(value):
    browser.element(value).perform(command.js.scroll_into_view)
