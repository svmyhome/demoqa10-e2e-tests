import json

from selene import browser, be, by
import allure
from allure import attachment_type
from allure_commons.types import Severity


def test_github_only_selene():
    browser.config.window_width = 1200
    browser.open('https://github.com/')

    browser.element(".search-input-container .input-button").click()
    browser.element("#query-builder-test").click().send_keys(
        'eroshenkoam/allure-example'
    ).press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element("#issues-tab").click()

    browser.element("#issue_76").should(be.visible)


def test_github_allure_steps_lambda():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Sarychev Vladimir')
    allure.dynamic.feature('Работа с репозиторием')
    allure.dynamic.story("Авторизованный пользователь может найти задачу")
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step('Настройка браузера и открытие главной страницы'):
        browser.config.window_width = 1200
        browser.open('https://github.com/')

    with allure.step('Поиск репозиитория'):
        browser.element(".search-input-container .input-button").click()
        browser.element("#query-builder-test").click().send_keys(
            'eroshenkoam/allure-example'
        ).press_enter()

    with allure.step('Переход в репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переход на вкладку с задачами'):
        browser.element("#issues-tab").click()

    with allure.step('Задача существует'):
        browser.element("#issue_76").should(be.visible)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Sarychev Vladimir')
@allure.feature('Работа с репозиторием')
@allure.story('Не авторизованный пользователь может найти задачу')
@allure.link('https://github.com', name='Testing')
def test_github_allure_steps_decorator():
    repo_name = 'eroshenkoam/allure-example'
    browser_open()
    search_repository(repo_name)
    go_to_repository(repo_name)
    click_issue_tab()
    assert_issue()


@allure.step('Настройка браузера и открытие главной страницы')
def browser_open():
    browser.config.window_width = 1200
    browser.open('https://github.com/')


@allure.step('Поиск репозиитория')
def search_repository(repo):
    browser.element(".search-input-container .input-button").click()
    browser.element("#query-builder-test").click().send_keys(repo).press_enter()


@allure.step('Переход в репозиторий')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Переход на вкладку с задачами')
def click_issue_tab():
    browser.element("#issues-tab").click()


@allure.step('Задача существует')
def assert_issue():
    browser.element("#issue_76").should(be.visible)


def test_attachments():
    allure.attach(
        'This is TEXT attachment', name="Text", attachment_type=attachment_type.TEXT
    )
    allure.attach(
        '<h1>This is HTML attachment</h1>',
        name="Html",
        attachment_type=attachment_type.HTML,
    )
    allure.attach(
        json.dumps({'key': 1, 'key2': 2}),
        name="Json",
        attachment_type=attachment_type.JSON,
    )
