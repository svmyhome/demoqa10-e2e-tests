import allure
import requests
from selene import browser

import config


def attach_png():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG,
    )


def attach_page_source():
    allure.attach(
        browser.driver.page_source,
        name='XML page',
        attachment_type=allure.attachment_type.XML,
    )


def attach_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.user_name, config.access_key),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
