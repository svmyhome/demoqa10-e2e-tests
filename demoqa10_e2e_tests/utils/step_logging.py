import json
import logging

import allure
import requests
from requests import Response
from curlify import to_curl


def response_logging(method, url, **kwargs):
    with allure.step(f'{method} {url}'):
        response: Response = requests.request(method, url=url, **kwargs)
        request_to_curl = to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except json.JSONDecodeError:
            if response.text:
                allure.attach(
                    body=response.text,
                    name='response',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt',
                )
            else:
                allure.attach(
                    body=None,
                    name='response',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt',
                )
        return response
